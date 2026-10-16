# Sugestão de cortes · 2026-10-15-sabatina-lula-globo-2turno

Gerado em 2026-10-16T00:44-03:00 por `ferramentas/sugerir-cortes.py`, **sem ler nenhuma checagem** (o arquivo de vereditos não é aberto). Critério: `recortes/SELECAO_DE_CORTES.md`. ⚠️ É sugestão: a decisão de quais cortes saem, e em que ordem aparecem no vídeo, é dele.

**6 cortes**, 81.4 s de trecho da emissora no total (teto 120 s; cada um até 15 s; 60 s entre um e outro). 225 janelas avaliadas.

## corte-01 · 04:14 a 04:27 · 12.8 s · `politica`

**Por quê:** critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 13 s, assunto politica  
**Pontos:** 3.0 (fato 3.0, confronto não, 0 trocas)  

- `A016` Lula: "Eu fui eleito tendo 70 deputados no meu partido de 513"
- `A017` Lula: "e tendo 9 senadores de 81"
- `A018` Lula: "E nós aprovamos 99% de tudo que a gente fez aqui no Congresso Nacional"

```bash
python -m checagem midia 2026-10-15-sabatina-lula-globo-2turno recortar corte-01 --inicio 253.75 --duracao 12.84 --motivo "critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 13 s, assunto politica" --caixa 94,62,1088,612
python ferramentas/derivar-recorte.py 2026-10-15-sabatina-lula-globo-2turno --de sabatina-completa --para corte-01 --inicio 253.75 --fim 266.59
```

## corte-02 · 08:01 a 08:15 · 13.2 s · `economia`

**Por quê:** critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 5 alegações checáveis em 13 s, assunto economia  
**Pontos:** 5.0 (fato 5.0, confronto não, 0 trocas)  

- `A036` Lula: "nós crescemos 20% com a China"
- `A037` Lula: "crescemos 15% com a Indonésia"
- `A038` Lula: "16% com a Alemanha"
- `A039` Lula: "13% com o Vietnã"
- `A040` Lula: "e crescemos em 50 países que nós visitamos, em média 10,5% a mais"

```bash
python -m checagem midia 2026-10-15-sabatina-lula-globo-2turno recortar corte-02 --inicio 481.29 --duracao 13.22 --motivo "critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 5 alegações checáveis em 13 s, assunto economia" --caixa 94,62,1088,612
python ferramentas/derivar-recorte.py 2026-10-15-sabatina-lula-globo-2turno --de sabatina-completa --para corte-02 --inicio 481.29 --fim 494.51
```

## corte-03 · 16:47 a 17:01 · 13.8 s · `justica`

**Por quê:** critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 14 s, assunto justica; confronto jornalista x entrevistado em justica; 1 troca de turno  
**Pontos:** 4.5 (fato 2.6, confronto sim, 1 trocas)  

- `A073` Renata Lo Prete: "que de fato, candidato, é o ministro até aqui mais implicado com o Daniel Vorcaro."
- `A074` Lula: "o Toffoli também está implicado"
- `A075` Lula: "o André Mendonça também está implicado"

```bash
python -m checagem midia 2026-10-15-sabatina-lula-globo-2turno recortar corte-03 --inicio 1006.87 --duracao 13.75 --motivo "critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 14 s, assunto justica; confronto jornalista x entrevistado em justica; 1 troca de turno" --caixa 94,62,1088,612
python ferramentas/derivar-recorte.py 2026-10-15-sabatina-lula-globo-2turno --de sabatina-completa --para corte-03 --inicio 1006.87 --fim 1020.62
```

## corte-04 · 35:52 a 36:05 · 12.5 s · `economia-internacional`

**Por quê:** critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 5 alegações checáveis em 12 s, assunto economia-internacional  
**Pontos:** 4.8 (fato 4.8, confronto não, 0 trocas)  

- `A145` Lula: "Devia 30 bilhões para o FMI"
- `A146` Lula: "Devia 30 bilhões para o FMI e não estava crescendo"
- `A147` Lula: "Quando eu deixei a presidência, o Brasil era a 7ª economia do mundo"
- `A148` Lula: "Fizemos uma reserva de 270 bilhões de dólares"
- `A149` Lula: "paguei os 30 bilhões do FMI"

```bash
python -m checagem midia 2026-10-15-sabatina-lula-globo-2turno recortar corte-04 --inicio 2152.13 --duracao 12.47 --motivo "critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 5 alegações checáveis em 12 s, assunto economia-internacional" --caixa 94,62,1088,612
python ferramentas/derivar-recorte.py 2026-10-15-sabatina-lula-globo-2turno --de sabatina-completa --para corte-04 --inicio 2152.13 --fim 2164.6
```

## corte-05 · 43:18 a 43:33 · 14.7 s · `saude`

**Por quê:** critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 15 s, assunto saude; confronto jornalista x entrevistado em saude; 3 trocas de turno  
**Pontos:** 5.1 (fato 2.4, confronto sim, 3 trocas)  

- `A182` Lula: "nós precisamos fazer o Brasil sorridente voltar a funcionar"
- `A183` Lula: "nós precisamos botar o Farmácia Popular voltar a funcionar"
- `A184` Renata Lo Prete: "o programa a que eu me referi é o Mais Especialistas, que ampliou o atendimento,"

```bash
python -m checagem midia 2026-10-15-sabatina-lula-globo-2turno recortar corte-05 --inicio 2598.18 --duracao 14.73 --motivo "critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 15 s, assunto saude; confronto jornalista x entrevistado em saude; 3 trocas de turno" --caixa 94,62,1088,612
python ferramentas/derivar-recorte.py 2026-10-15-sabatina-lula-globo-2turno --de sabatina-completa --para corte-05 --inicio 2598.18 --fim 2612.91
```

## corte-06 · 45:26 a 45:41 · 14.4 s · `programas-sociais`

**Por quê:** critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 14 s, assunto programas-sociais; 1 troca de turno  
**Pontos:** 3.0 (fato 2.6, confronto não, 1 trocas)  

- `A191` Lula: "como nós fizemos com a energia elétrica. quem consome até 80 não paga e quem consome até 120 paga apenas uma diferença,"
- `A192` Lula: "Nós estamos distribuindo o gás para 17 milhões de pessoas"
- `A193` Lula: "sabendo que nós pagamos o gás."

```bash
python -m checagem midia 2026-10-15-sabatina-lula-globo-2turno recortar corte-06 --inicio 2726.31 --duracao 14.39 --motivo "critério pré-registrado (recortes/SELECAO_DE_CORTES.md): 3 alegações checáveis em 14 s, assunto programas-sociais; 1 troca de turno" --caixa 94,62,1088,612
python ferramentas/derivar-recorte.py 2026-10-15-sabatina-lula-globo-2turno --de sabatina-completa --para corte-06 --inicio 2726.31 --fim 2740.7
```

## As outras candidatas (as de maior pontuação)

| Janela | Duração | Pontos | Checáveis | Confronto | Trocas | Assunto |
|---|---:|---:|---:|---|---:|---|
| 43:18 a 43:33 | 14.7 s | 5.1 | 3 | saude | 3 | saude |
| 08:01 a 08:15 | 13.2 s | 5.0 | 5 | · | 0 | economia |
| 07:56 a 08:09 | 13.4 s | 5.0 | 5 | · | 0 | economia |
| 35:52 a 36:05 | 12.5 s | 4.8 | 5 | · | 0 | economia-internacional |
| 16:47 a 17:01 | 13.8 s | 4.5 | 3 | justica | 1 | justica |
| 43:22 a 43:33 | 11.2 s | 4.3 | 2 | saude | 3 | saude |
| 08:01 a 08:09 | 8.1 s | 4.0 | 4 | · | 0 | economia |
| 08:04 a 08:15 | 10.6 s | 4.0 | 4 | · | 0 | economia |
| 35:52 a 36:03 | 10.7 s | 4.0 | 4 | · | 0 | economia-internacional |
| 07:56 a 08:08 | 11.6 s | 4.0 | 4 | · | 0 | economia |
| 08:06 a 08:20 | 14.2 s | 4.0 | 4 | · | 0 | economia |
| 35:45 a 36:00 | 14.3 s | 4.0 | 4 | · | 0 | economia |
| 07:53 a 08:08 | 14.5 s | 4.0 | 4 | · | 0 | economia |
| 35:56 a 36:09 | 12.3 s | 3.8 | 4 | · | 0 | economia-internacional |
| 36:03 a 36:15 | 12.5 s | 3.8 | 4 | · | 0 | economia-internacional |
