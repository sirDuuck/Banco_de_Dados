const fs = require('fs');
const csv = rqueire('csv-parser');
const axios = require('axios');


//função para consulta a api
async function consultarAPI(cnpjBasico, cnpjOrdem, cnpjDiv) {
    const apiUrl = 'URL_DA_SUA_API';

    //realizar consulta
    try {
        const response = await axios.get(apiUrl, {
            params: {
                cnpjBasico,
                cnpjOrdem,
                cnpjDiv,
            },
        });

        const data = response.data;
        
        if(data.existe) {
            //se existir= update
            console.log('Fazendo o update na API para', cnpjBasico);
            //implementar codigo para fazr oupdate aqui
        } else {
            //se a informação nao existir, fazça um post na api
            console.error('Erro ao consultar a API:', error);
        }
    }

    //Funçao para ler arquivo csv
    function lerCSV() {
        fs.createReadStream('Arquivo.csv')
        .pipe(csv())
        .on('data', (row)=>{
            const cnpjBasico = row['CNPJ_Basico']; // substitua pelo nomes corretos
            const cnpjOrdem = row['CNPJ_Ordem'];
            const cnpjDiv = row['CNPJ_Div'];

            consultarAPI(cnpjBasico, cnpjOrdem, cnpjDiv);
        })
        .on('end', () => {
            console,log('Processamento do CSV concluido.');
        });
    }}

    // Inicie a leitura do cvs
    lerCSV();