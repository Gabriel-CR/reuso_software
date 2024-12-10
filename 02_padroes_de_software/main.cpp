#include <iostream>
#include <memory>
#include <string>

using namespace std;

// Produto - Interface comum
// Define uma interface base para todos os tipos de notificações. 
// Classes derivadas devem implementar o método notifyUser().
class Notification
{
public:
  // Método puramente virtual que deve ser implementado pelas subclasses.
  // Representa a ação de notificar o usuário.
  virtual void notifyUser() const = 0;

  // Destrutor virtual para garantir que a destruição correta ocorra 
  // ao lidar com objetos derivados via ponteiros base.
  virtual ~Notification() = default; 
};


// Produtos Concretos
// Implementam a interface Notification para criar notificações específicas.

class SMSNotification : public Notification {
public:
  // Sobrescreve o método virtual notifyUser() para realizar as adaptações
  // necessárias aos envios de SMS
  void notifyUser() const override {
    cout << "#####################################\n"
         << "Enviando uma notificação por SMS\n" 
         << "#####################################\n";
  }
};

class EmailNotification : public Notification {
public:
  // Sobrescreve o método virtual notifyUser() para realizar as adaptações
  // necessárias aos envios de e-mail
  void notifyUser() const override {
    cout << "#####################################\n"
         << "Enviando uma notificação por E-mail\n" 
         << "#####################################\n";
  }
};

class WhatsAppNotification : public Notification {
public:
  // Sobrescreve o método virtual notifyUser() para realizar as adaptações
  // necessárias aos envios de Whats App
  void notifyUser() const override {
    cout << "#######################################\n"
         << "Enviando uma notificação por Whats App\n" 
         << "#######################################\n";
  }
};

// Creator - Classe base para a fábrica
class NotificationFactory
{
public:
  virtual unique_ptr<Notification> createNotification() const = 0; // Método Factory
  virtual ~NotificationFactory() = default;

  void sendNotification() const
  {
    auto notification = createNotification();
    notification->notifyUser();
  }
};

// Creators Concretos
// As classes abaixo implementam o método createNotification() da fábrica base,
// fornecendo instâncias específicas de notificações para cada caso.

class SMSNotificationFactory : public NotificationFactory {
public:
  // Este método cria e retorna uma instância de SMSNotification.
  // Ele utiliza make_unique para garantir a alocação segura e eficiente de memória.
  // A fábrica encapsula completamente a lógica de criação, de modo que o cliente
  // não precisa conhecer os detalhes da implementação do SMSNotification.
  unique_ptr<Notification> createNotification() const override {
    return make_unique<SMSNotification>();
  }
};

class EmailNotificationFactory : public NotificationFactory {
public:
  // Este método cria e retorna uma instância de EmailNotification.
  // Isso garante que qualquer solicitação de notificação por e-mail
  // seja gerenciada exclusivamente por essa fábrica concreta.
  // O método assegura que o cliente receba um objeto válido e configurado corretamente.
  unique_ptr<Notification> createNotification() const override {
    return make_unique<EmailNotification>();
  }
};

class WhatsAppNotificationFactory : public NotificationFactory {
public:
  // Este método cria e retorna uma instância de WhatsAppNotification.
  // Ele abstrai o processo de criação de notificações via WhatsApp,
  // isolando a lógica para evitar que o cliente precise manipular diretamente o objeto.
  // Esse design facilita a manutenção e possíveis mudanças na implementação do WhatsAppNotification.
  unique_ptr<Notification> createNotification() const override {
    return make_unique<WhatsAppNotification>();
  }
};


// Demonstração de uso
int main()
{
  unique_ptr<NotificationFactory> factory;

  // Escolhendo dinamicamente o tipo de notificação
  string notificationType = "";
  cout << "Escolha uma opção de notificação\n" 
       << "[1] SMS\n"
       << "[2] E-mail\n"
       << "[3] Whats App\n"
       << "> ";

  cin >> notificationType;

  if (notificationType == "1")
  {
    factory = make_unique<SMSNotificationFactory>();
  }
  else if (notificationType == "2")
  {
    factory = make_unique<EmailNotificationFactory>();
  }
  else if (notificationType == "3")
  {
    factory = make_unique<WhatsAppNotificationFactory>();
  }
  else
  {
    cerr << "Tipo de notificação não suportado" << endl;
    return 1;
  }

  // Enviando a notificação
  factory->sendNotification();

  return 0;
}