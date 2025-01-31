# Graph Rag Web Viewer – Micro-Relatório

## 1. Identificação do Projeto
- **Título do Projeto:** Graph Rag Web Viewer
- **Nome do Aluno:** Artur Ribeiro
- **Data de Entrega:** 31/01/2025

---

## 2. Objetivos e Contexto

### Breve Descrição
Este projeto consiste no desenvolvimento de uma aplicação web para carregar ficheiros de texto, indexá-los através do Graph Rag da Microsoft e visualizá-los como um grafo interativo. Além disso, a aplicação permite realizar perguntas ao grafo e obter respostas contextuais.

### Justificativa/Contexto
O objetivo principal é facilitar a organização e consulta de grandes volumes de informação textual, permitindo aos utilizadores navegar de forma mais intuitiva pelos documentos carregados. Esta solução pode ser útil para empresas que precisam estruturar documentos internos, tornando a pesquisa de informações mais eficiente.

---

## 3. Atividades Desenvolvidas

### Tecnologias e Ferramentas Utilizadas
- **Backend:** Python (FastAPI), Uvicorn, NetworkX, Flask-CORS
- **Frontend:** React.js, Axios, Vis-Network, React-Dropzone
- **Desenvolvimento:** VS Code 

### Descrição Sintética das Tarefas
- **Configuração do ambiente:** Instalação de bibliotecas e criação da estrutura do projeto.
- **Desenvolvimento do backend:** Implementação das rotas para upload de ficheiros, indexação no grafo e sistema de perguntas.
- **Criação do frontend:** Interface para upload de ficheiros, exibição do grafo e envio de perguntas.
- **Integração entre frontend e backend:** Comunicação via Axios e testes de conectividade.
- **Correção de erros e testes:** Ajustes de CORS, debug de erros de conexão, validação da interface e testes finais.
- **Documentação e refinamento:** Escrever o README e este relatório.

---

## 4. Contributos Individuais
Como este projeto foi realizado individualmente, todas as tarefas foram executadas por mim. No entanto, algumas etapas foram otimizadas com o apoio de **IA**, incluindo:
- **Pesquisa sobre o Graph Rag da Microsoft** – Utilização de IA para entender o funcionamento do serviço e explorar alternativas de indexação.
- **Correção de erros e debugging** – Identificação e resolução de problemas em Axios, FastAPI e integração frontend-backend.
- **Otimização do código** – Sugestões de melhorias para estruturação e organização do código em Python e React.


## 5. Organização e Metodologia de Trabalho

### Planeamento e Cronograma
- O desenvolvimento foi dividido em etapas lógicas (**backend → frontend → integração → testes**).
- Cada funcionalidade foi testada separadamente antes da integração.

### Comunicação e Articulação
- Como trabalhei sozinho, utilizei anotações pessoais e planejamento manual para organizar as tarefas.

### Forma de Integração do Código
- Todo o código foi organizado localmente e testado manualmente antes da finalização.



## 6. Principais Dificuldades e Aprendizagens

### Dificuldades Encontradas
- Configuração inicial do **CORS** no backend FastAPI.
- Conexão entre frontend (**React**) e backend (**FastAPI**), devido a erros de portas e permissões de acesso.

### Aprendizagens e Evolução
- Melhor compreensão de **FastAPI** e sua interação com o React.
- Aprendizado sobre **Axios** e a comunicação entre frontend e backend.
- Experiência na construção de uma interface visual interativa para exibição de grafos.

---

## 7. Conclusão e Próximos Passos

### Estado Final do Projeto
O projeto está **funcional**, permitindo:
- **Upload de ficheiros** de texto.
- **Indexação automática** dos ficheiros no **grafo**.
- **Visualização interativa** dos nós do grafo.
- **Pesquisa inteligente** dentro do grafo, respondendo perguntas com base nos documentos carregados.

### Sugestões de Futuro
- Melhorar a interface gráfica do frontend com bibliotecas mais avançadas.
- Adicionar suporte para mais tipos de ficheiros além de `.txt`.
- Integrar autenticação de utilizadores para maior segurança.

---

## 8. Referências
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React.js Documentation](https://react.dev/)
- [Axios HTTP Requests](https://axios-http.com/)
- [Vis-Network para visualização de grafos](https://visjs.org/)

---

## Observações Finais
Este micro-relatório sintetiza a organização e desenvolvimento do projeto **Graph Rag Web Viewer**, descrevendo como foi estruturado, as dificuldades encontradas e as aprendizagens obtidas. A experiência adquirida com **FastAPI, React e manipulação de grafos** foi extremamente valiosa e reforçou conceitos essenciais de desenvolvimento web. 
