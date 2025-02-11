public class Main {
	public static void main(String[] args) throws Exception {
		System.out.println("=== Testando CRUD com InMemoryRepository ===");

		InMemoryRepository<Produto> memoryProdutoRepo = new InMemoryRepository<>();

		Produto p1 = new Produto(1, "Laptop", 3000.0);
		Produto p2 = new Produto(2, "Mouse", 50.0);

		// CREATE
		memoryProdutoRepo.save(p1);
		memoryProdutoRepo.save(p2);

		// READ
		System.out.println("Lista de Produtos em Memória:");
		for (Produto p : memoryProdutoRepo.findAll()) {
			System.out.println(p);
		}

		// UPDATE
		Produto produtoAtualizado = new Produto(1, "Laptop Gamer", 5000.0);
		memoryProdutoRepo.update(produtoAtualizado);
		System.out.println("Produto atualizado na memória: " + memoryProdutoRepo.findById(1));

		// DELETE
		memoryProdutoRepo.delete(2);
		System.out.println("Lista de Produtos após remoção em Memória:");
		for (Produto p : memoryProdutoRepo.findAll()) {
			System.out.println(p);
		}

		// ------------------------------------------------------------

		System.out.println("\n=== Testando CRUD com InFileRepository ===");

		InFileRepository<Produto> fileProdutoRepo = new InFileRepository<>("produtos.txt");

		// CREATE
		fileProdutoRepo.save(p1);
		fileProdutoRepo.save(p2);

		// READ
		System.out.println("Buscando Produto ID 1 no Arquivo:");
		fileProdutoRepo.findById(1);

		System.out.println("Lista de Produtos no Arquivo:");
		fileProdutoRepo.findAll();

		// UPDATE
		fileProdutoRepo.update(produtoAtualizado);
		System.out.println("Produto atualizado no arquivo: ");
		fileProdutoRepo.findById(1);

		// DELETE
		fileProdutoRepo.delete(2);
		System.out.println("Lista de Produtos no Arquivo após remoção:");
		fileProdutoRepo.findAll();
	}
}
