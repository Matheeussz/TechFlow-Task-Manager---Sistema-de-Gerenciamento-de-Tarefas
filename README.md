# TechFlow Task Manager - Sistema de Gerenciamento de Tarefas

## 🎯 Objetivo do Projeto
Este projeto consiste no desenvolvimento de um sistema de gerenciamento de tarefas em tempo real para uma startup de logística, visando otimizar o fluxo de trabalho, priorizar demandas críticas e monitorar a produtividade da equipe.

## 📋 Escopo Inicial
- Autenticação de usuários (Login).
- CRUD de Tarefas (Criar, Ler, Atualizar e Deletar tarefas).
- Atribuição de responsáveis e prazos para as tarefas.

## 🚀 Metodologia Adotada
Utilizamos a metodologia **Scrum/Kanban** para a gestão do projeto. O acompanhamento é feito visualmente através do GitHub Projects, dividindo as atividades em ciclos de entrega e garantindo transparência.

## ⚠️ Gestão de Mudanças (Alteração de Escopo)
O cliente (startup de logística) solicitou uma alteração urgente no escopo do projeto após o planejamento inicial. Foi identificada a necessidade crítica de os utilizadores conseguirem categorizar e filtrar as tarefas com base em **"Rotas de Entrega" ou "Regiões"**, permitindo aos motoristas focar apenas nas tarefas da sua área de atuação. 

**Impacto no projeto:** Esta mudança exige a alteração da base de dados (adicionar o campo `regiao` na tabela de tarefas) e a atualização do ecrã de listagem para incluir filtros. As tarefas impactadas foram movidas de volta para a coluna "A Fazer" no Kanban para serem reavaliadas.

---

## 📝 Respostas às Questões Norteadoras do Projeto

### 1. Quais são as principais causas de falhas em projetos ágeis e como o GitHub pode ajudar a mitigá-las?
* **Falhas de comunicação e falta de transparência:** Projetos falham quando a equipa não sabe o que cada membro está a fazer. O **GitHub Projects (Kanban)** resolve isso ao centralizar o progresso de forma visual.
* **Aumento descontrolado do escopo (Scope Creep):** Alterações sem registo perdem o controlo do prazo. O uso de **GitHub Issues** e a documentação destas mudanças no `README.md` garantem que o histórico e o impacto estejam claros para todos.
* **Falta de qualidade e código quebrado:** Sem testes frequentes, integrar o trabalho de vários programadores gera erros. O GitHub mitiga isso através de **Pull Requests** com revisões de código obrigatórias.

### 2. Quem são os principais beneficiados por um sistema de gerenciamento ágil e como eles utilizam as funcionalidades desenvolvidas?
* **Gestores de Projeto / Scrum Masters:** Utilizam o quadro Kanban do GitHub para monitorizar gargalos, distribuir tarefas e acompanhar a velocidade da equipa.
* **Desenvolvedores:** Beneficiam da clareza das tarefas descritas nas *Issues*, sabendo exatamente o que precisa de ser feito, reduzindo o retrabalho.
* **O Cliente Final (Startup de Logística):** Consegue acompanhar o progresso real do sistema e recebe entregas de valor mais rapidamente (iterações/sprints), garantindo que o produto final atende às suas necessidades.

### 3. Como o uso de ferramentas de controle de qualidade, como GitHub Actions, pode garantir a entrega de um software confiável?
O GitHub Actions funciona como um inspetor de qualidade automatizado (CI - Integração Contínua). Sempre que um programador envia código novo (*Push*), o Actions executa automaticamente a suite de testes configurada num ambiente isolado. Se o novo código introduzir um erro ou quebrar uma função antiga, o pipeline falha imediatamente, impedindo que o código com erros chegue à versão de produção (`main`).

### 4. Quais são os principais desafios ao implementar mudanças em um projeto ágil e como lidar com eles?
* **Gestão de prioridades:** O maior desafio é encaixar o novo pedido sem atrasar o que já estava prometido. Lida-se com isto reavaliando o Kanban e movendo itens menos urgentes para o "Backlog".
* **Alinhamento da equipa:** Mudanças repentinas podem confundir os programadores. Lida-se com isto atualizando os critérios de aceitação nas *Issues* do GitHub e realizando breves reuniões de alinhamento (*Daily Scrum*) para explicar a alteração.
