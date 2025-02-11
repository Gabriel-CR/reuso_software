import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InMemoryRepository<T extends Identifiable> implements CrudRepository<T> {
  private final Map<Integer, T> storage = new HashMap<>();

  @Override
  public void save(T entity) {
    storage.put(entity.getId(), entity);
  }

  @Override
  public T findById(int id) {
    return storage.get(id);
  }

  @Override
  public void update(T entity) {
    if (storage.containsKey(entity.getId())) {
      storage.put(entity.getId(), entity);
    } else {
      System.out.println("Entidade com ID " + entity.getId() + " não encontrada.");
    }
  }

  @Override
  public void delete(int id) {
    storage.remove(id);
  }

  @Override
  public List<T> findAll() {
    return new ArrayList<>(storage.values());
  }
}
