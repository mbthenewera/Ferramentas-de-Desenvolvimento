# DevTools API

![Node.js](https://img.shields.io/badge/Node.js-API-339933?style=flat-square&logo=node.js&logoColor=white)
![Status](https://img.shields.io/badge/status-portfolio-111111?style=flat-square)

API utilitária para desenvolvedores com endpoints de hash, análise de extensões, resumo de texto e inspeção simples de payloads.

## English

Developer utility API with endpoints for hashing, extension analysis, text summaries and simple payload inspection.

## Por que esse projeto é bom para currículo

- Mostra criação de API REST com Node.js.
- Tem endpoints claros e testáveis.
- Resolve problemas reais de rotina dev.
- Pode evoluir com testes, Docker e CI.

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/health` | Status da API |
| POST | `/hash` | Gera SHA-256 de um texto |
| POST | `/text-summary` | Conta caracteres, palavras e linhas |
| POST | `/extension-stats` | Conta extensões de uma lista de arquivos |

## Rodar localmente

```bash
npm install
npm run dev
```

## Exemplo

```bash
curl -X POST http://localhost:3000/hash \
  -H "Content-Type: application/json" \
  -d '{"value":"Mateus"}'
```

## Roadmap

- [ ] Adicionar testes com Vitest
- [ ] Adicionar Dockerfile
- [ ] Publicar documentação OpenAPI
- [ ] Configurar GitHub Actions
