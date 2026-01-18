# ScriptBoleto

## 📋 Motivação

Este projeto nasceu da necessidade de **automatizar uma tarefa manual repetitiva e propensa a erros**. Anteriormente, o processo de pagamento de contas era realizado manualmente:

1. Acessar o portal do provedor de internet
2. Realizar login com CPF
3. Navegar até a seção de boletos
4. Baixar o boleto do mês atual
5. Enviar o boleto por e-mail para o pagador final

O **ScriptBoleto** elimina essa necessidade ao automatizar completamente este fluxo, economizando tempo, reduzindo erros humanos e garantindo que os boletos sejam entregues de forma consistente e pontual.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10** - Linguagem base do projeto
- **Selenium** - Automação de navegação web e interação com o portal
- **SMTP** - Protocolo para envio de e-mails
- **Logging** - Rastreamento e registro de eventos
- **GitHub Actions** - Agendamento e automação de execuções periódicas

## ✨ Destaques da Arquitetura

### Modularização
O projeto segue uma estrutura modular bem definida, separando responsabilidades:
- **Módulo de autenticação** - Gerencia login no portal
- **Módulo de extração** - Localiza e faz download do boleto
- **Módulo de notificação** - Envia e-mails com o boleto anexado
- **Configurações centralizadas** - Facilita manutenção e adaptação

### Segurança
- Credenciais armazenadas de forma segura (variáveis de ambiente ou arquivo de configuração cifrado)
- Evita exposição de dados sensíveis no código

### Rastreabilidade
- Sistema robusto de logs que registra cada etapa do processo
- Facilita debug e auditoria de execuções

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8 ou superior
- Git instalado
- Uma conta de e-mail Gmail SMTP configurada
- Uma conta no GitHub

### Instalação

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

### Configuração Local

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

### Execução

**Executar o script uma única vez:**
```bash
python main.py
```

### Automação com GitHub Actions

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

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
