import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class InFileRepository<T extends Identifiable> implements CrudRepository<T> {
  private final String filename;
  private int currentId = 1;

  public InFileRepository(String filename) {
    this.filename = filename;
  }

  @Override
  public void save(T entity) {
    try (FileWriter writer = new FileWriter(filename, true);
        BufferedWriter bw = new BufferedWriter(writer)) {
      bw.write(currentId++ + "," + entity.toString());
      bw.newLine();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  @Override
  public T findById(int id) {
    try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
      String line;
      while ((line = br.readLine()) != null) {
        String[] parts = line.split(",", 2);
        if (Integer.parseInt(parts[0]) == id) {
          System.out.println("Encontrado: " + parts[1]);
          return null; // Você deve modificar para converter `parts[1]` na sua entidade T
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
    return null;
  }

  @Override
  public void update(T entity) {
    List<String> updatedLines = new ArrayList<>();
    boolean found = false;

    try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
      String line;
      while ((line = br.readLine()) != null) {
        String[] parts = line.split(",", 2);
        if (Integer.parseInt(parts[0]) == entity.getId()) {
          updatedLines.add(entity.getId() + "," + entity.toString());
          found = true;
        } else {
          updatedLines.add(line);
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    if (found) {
      try (BufferedWriter bw = new BufferedWriter(new FileWriter(filename))) {
        for (String updatedLine : updatedLines) {
          bw.write(updatedLine);
          bw.newLine();
        }
      } catch (IOException e) {
        e.printStackTrace();
      }
    } else {
      System.out.println("Entidade com ID " + entity.getId() + " não encontrada.");
    }
  }

  @Override
  public void delete(int id) {
    List<String> updatedLines = new ArrayList<>();
    boolean deleted = false;

    try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
      String line;
      while ((line = br.readLine()) != null) {
        String[] parts = line.split(",", 2);
        if (Integer.parseInt(parts[0]) != id) {
          updatedLines.add(line);
        } else {
          deleted = true;
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    if (deleted) {
      try (BufferedWriter bw = new BufferedWriter(new FileWriter(filename))) {
        for (String updatedLine : updatedLines) {
          bw.write(updatedLine);
          bw.newLine();
        }
      } catch (IOException e) {
        e.printStackTrace();
      }
    } else {
      System.out.println("Entidade com ID " + id + " não encontrada.");
    }
  }

  @Override
  public List<T> findAll() {
    List<T> entities = new ArrayList<>();
    try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
      String line;
      while ((line = br.readLine()) != null) {
        System.out.println("Lido do arquivo: " + line);
        // Aqui você precisa converter `line` para um objeto T
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
    return entities;
  }
}
