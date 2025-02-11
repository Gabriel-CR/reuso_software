public class Produto implements Identifiable {
  private int id;
  private String nome;
  private double preco;

  public Produto(int id, String nome, double preco) {
    this.id = id;
    this.nome = nome;
    this.preco = preco;
  }

  public int getId() {
    return id;
  }

  @Override
  public String toString() {
    return "Produto{" + "id=" + id + ' ' + "nome='" + nome + '\'' + ", preco=" + preco + '}';
  }
}
