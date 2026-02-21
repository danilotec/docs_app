import pdfList  from './list.js';

const pdfFolder = 'pdfs/'; // Pasta onde estão os PDFs no seu repositório
let allPdfs = [];

function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}



function createPdfCard(pdf) {
    return `
    <div class="pdf-card">
        <i class="fa-solid fa-file-pdf"></i>
        <h3>${pdf.name}</h3>
        <a href="${pdfFolder}${pdf.filename}" class="btn-download" target="_blank">Abrir PDF</a>
    </div>
`;
}

function renderPdfs(pdfs) {
    const grid = document.getElementById('pdfGrid');
    
    if (pdfs.length === 0) {
        grid.innerHTML = '<div class="no-results">📭 Nenhum PDF encontrado</div>';
        return;
    }
    
    grid.innerHTML = pdfs.map(createPdfCard).join('');
}

function filterPdfs(searchTerm) {
    const filtered = allPdfs.filter(pdf => 
        pdf.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    renderPdfs(filtered);
}

// Inicialização
function init() {
    allPdfs = pdfList;
    
    // Simular loading
    setTimeout(() => {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('pdfGrid').style.display = 'grid';
        renderPdfs(allPdfs);
    }, 1000);

    // Setup search
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
        filterPdfs(e.target.value);
    });
}

// Iniciar quando a página carregar
document.addEventListener('DOMContentLoaded', init);