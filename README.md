# 🖥️ laptop-logs

**Versão:** 0.1.0
**Status:** Em desenvolvimento
**Uso:** Pessoal
**Testado em:** Arch Linux (KDE Plasma)

---

## 📌 Sobre o projeto

O **laptop-logs** é um sistema leve de monitoramento de eventos do notebook.

Ele registra automaticamente ações e eventos do sistema em tempo real, salvando tudo em arquivos de log locais para auditoria pessoal, análise de uso e segurança básica.

> ⚠️ Projeto em fase inicial, sujeito a mudanças constantes.

---

## 🧠 Eventos monitorados

Atualmente o sistema captura os seguintes eventos:

* 💻 Tampa do notebook

  * Abrir
  * Fechar

* 🔐 Sessão do sistema

  * Bloqueada
  * Desbloqueada

* 🚨 Tentativas de acesso

  * Senha incorreta

* 💤 Estado da tela

  * Suspenso
  * Retomado

---

## 📷 Captura de imagens

O sistema utiliza **OpenCV** para capturar imagens da câmera em determinados eventos.

As imagens são salvas localmente e associadas aos logs correspondentes.

---

## ⚙️ Tecnologias utilizadas

* 🐍 Python (base do sistema)
* 📷 OpenCV (captura de imagens da câmera)
* 🪵 Sistema de logs em arquivo `.txt`

---

## 🧾 Formato dos logs

Os logs seguem o padrão:

```id="ve9c54"
[EVENTO] - YYYY-MM-DD HH:MM:SS.microseconds - CAMINHO_DA_IMAGEM
```

---

### 📌 Exemplo real

```id="3s7k8x"
[SESSÃO BLOQUEADA] - 2026-06-27 20:06:15.157199 - PHOTOS/PHOTO_3_27-06-2026_20:06:15.JPG
```

---

### 🧠 Estrutura detalhada

Cada linha de log contém:

#### 1. 🔔 Evento

Tipo de ação detectada pelo sistema:

* SESSÃO BLOQUEADA
* SESSÃO DESBLOQUEADA
* TAMPA ABERTA
* TAMPA FECHADA
* TENTATIVA DE ACESSO (SENHA INCORRETA)
* TELA SUSPENSA
* TELA RETOMADA

---

#### 2. 🕒 Timestamp

Data e hora exata do evento:

```
2026-06-27 20:06:15.157199
```

---

#### 3. 📷 Snapshot (opcional)

Caminho da imagem capturada no momento do evento:

```
PHOTOS/PHOTO_3_27-06-2026_20:06:15.JPG
```

> ℹ️ Todos eventos captura uma imagem da camera.

---

## 💾 Armazenamento

Todos os eventos são armazenados em arquivos `.txt` locais.

O formato foi projetado para ser:

* Simples de ler
* Fácil de processar via scripts
* Compatível com futuras análises e dashboards

---

## 🧪 Ambiente de teste

Sistema testado em:

* 🐧 Arch Linux
* 🧩 KDE Plasma 6.7.1 (plasmashell)
* 💻 Kernel Linux 7.0.12-arch1-1
* 🖥️ Dell Inspiron 15 3520

---

## ⚠️ Observações importantes

* Projeto ainda **muito imaturo**
* Pode conter bugs e comportamentos inesperados
* Estrutura de logs pode mudar no futuro
* Uso recomendado apenas para testes pessoais

---

## 🤝 Contribuição

Sinta-se livre para:

* Fazer fork
* Abrir issues
* Sugerir melhorias
* Enviar pull requests

Esse é um projeto pessoal, mas contribuições são bem-vindas.

---

# 📄 Licença

Este projeto está licenciado sob a MIT License.

Isso significa que você pode usar, copiar, modificar e distribuir o software livremente, desde que mantenha os devidos créditos e a nota de licença.

O software é fornecido “como está”, sem garantias de qualquer tipo.