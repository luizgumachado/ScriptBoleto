# ScriptBoleto

**[English](#english) | [Português](#português)**

---

## Português

### 📋 Motivação

Este projeto nasceu da necessidade de **automatizar uma tarefa manual repetitiva e propensa a erros**. Anteriormente, o processo de pagamento de contas era realizado manualmente:

1. Acessar o portal do provedor de internet
2. Realizar login com CPF
3. Navegar até a seção de boletos
4. Baixar o boleto do mês atual
5. Enviar o boleto por e-mail para o pagador final

O **ScriptBoleto** elimina essa necessidade ao automatizar completamente este fluxo, economizando tempo, reduzindo erros humanos e garantindo que os boletos sejam entregues de forma consistente e pontual.

### 🛠️ Tecnologias Utilizadas

- **Python 3.10** - Linguagem base do projeto
- **Selenium** - Automação de navegação web e interação com o portal
- **SMTP** - Protocolo para envio de e-mails
- **Logging** - Rastreamento e registro de eventos
- **GitHub Actions** - Agendamento e automação de execuções periódicas

### ✨ Destaques da Arquitetura

#### Modularização
O projeto segue uma estrutura modular bem definida, separando responsabilidades:
- **Módulo de autenticação** - Gerencia login no portal
- **Módulo de extração** - Localiza e faz download do boleto
- **Módulo de notificação** - Envia e-mails com o boleto anexado
- **Configurações centralizadas** - Facilita manutenção e adaptação

#### Segurança
- Credenciais armazenadas de forma segura (variáveis de ambiente ou arquivo de configuração cifrado)
- Evita exposição de dados sensíveis no código

#### Rastreabilidade
- Sistema robusto de logs que registra cada etapa do processo
- Facilita debug e auditoria de execuções

### 🚀 Como Usar

#### Pré-requisitos
- Python 3.8 ou superior
- Git instalado
- Uma conta de e-mail Gmail SMTP configurada
- Uma conta no GitHub

#### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/luizgumachado/ScriptBoleto.git
cd ScriptBoleto
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

#### Configuração Local

1. **Copie o arquivo de exemplo de configuração:**
```bash
copy .env.example .env
```

2. **Abra o arquivo `.env` e configure as credenciais:**
```
CPF_PROVEDOR=seu_cpf
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_DESTINATARIO=pagador@example.com
SENHA_REMETENTE=sua_senha_app
```

#### Execução

**Executar o script uma única vez:**
```bash
python main.py
```

#### Automação com GitHub Actions

Este projeto utiliza **GitHub Actions** para executar automaticamente o script todos os meses, no dia 09.

**Configuração:**

1. Acesse **Settings > Secrets and variables > Actions** no repositório
2. Adicione os seguintes secrets:
   - `CPF_PROVEDOR`
   - `EMAIL_REMETENTE`
   - `EMAIL_DESTINATARIO`
   - `SENHA_REMETENTE`

3. O workflow está configurado em `.github/workflows/` e será executado automaticamente conforme agendado

O GitHub Actions gerencia toda a execução sem necessidade de configurar tarefas localmente!

---

## English

### 📋 Motivation

This project was born out of the need to **automate a repetitive and error-prone manual task**. Previously, the bill payment process was done manually:

1. Access the internet provider's portal
2. Log in with CPF
3. Navigate to the billing section
4. Download the current month's bill
5. Send the bill by email to the final payer

**ScriptBoleto** eliminates this need by completely automating this workflow, saving time, reducing human errors, and ensuring that bills are delivered consistently and on time.

### 🛠️ Technologies Used

- **Python 3.10** - Project base language
- **Selenium** - Web automation and portal interaction
- **SMTP** - Email sending protocol
- **Logging** - Event tracking and recording
- **GitHub Actions** - Scheduling and automation of periodic executions

### ✨ Architecture Highlights

#### Modularity
The project follows a well-defined modular structure, separating responsibilities:
- **Authentication module** - Manages portal login
- **Extraction module** - Locates and downloads the bill
- **Notification module** - Sends emails with the bill attached
- **Centralized configurations** - Facilitates maintenance and adaptation

#### Security
- Credentials stored securely (environment variables or encrypted configuration file)
- Prevents exposure of sensitive data in the code

#### Traceability
- Robust logging system that records each step of the process
- Facilitates debugging and execution auditing

### 🚀 How to Use

#### Prerequisites
- Python 3.8 or higher
- Git installed
- A Gmail SMTP account configured
- A GitHub account

#### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/luizgumachado/ScriptBoleto.git
cd ScriptBoleto
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
```

3. **Activate the virtual environment:**

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

#### Local Configuration

1. **Copy the example configuration file:**
```bash
copy .env.example .env
```

2. **Open the `.env` file and configure the credentials:**
```
CPF_PROVEDOR=your_cpf
EMAIL_REMETENTE=your_email@gmail.com
EMAIL_DESTINATARIO=payer@example.com
SENHA_REMETENTE=your_app_password
```

#### Execution

**Run the script once:**
```bash
python main.py
```

#### Automation with GitHub Actions

This project uses **GitHub Actions** to automatically run the script every month on the 9th.

**Configuration:**

1. Go to **Settings > Secrets and variables > Actions** in your repository
2. Add the following secrets:
   - `CPF_PROVEDOR`
   - `EMAIL_REMETENTE`
   - `EMAIL_DESTINATARIO`
   - `SENHA_REMETENTE`

3. The workflow is configured in `.github/workflows/` and will run automatically as scheduled

GitHub Actions manages the entire execution without needing to configure local tasks!

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
