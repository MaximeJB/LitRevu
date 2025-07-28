document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.alert');
    
    messages.forEach(function(message) {
        // Ajouter un bouton de fermeture
        const closeBtn = document.createElement('span');
        closeBtn.innerHTML = '&times;';
        closeBtn.className = 'close-btn';
        closeBtn.style.cssText = `
            position: absolute;
            top: 5px;
            right: 10px;
            cursor: pointer;
            font-size: 20px;
            font-weight: bold;
        `;
        
        closeBtn.addEventListener('click', function() {
            message.style.display = 'none';
        });
        
        message.appendChild(closeBtn);
        
        // Auto-dismiss après 5 secondes
        setTimeout(function() {
            if (message.style.display !== 'none') {
                message.style.opacity = '0';
                setTimeout(function() {
                    message.style.display = 'none';
                }, 300);
            }
        }, 5000);
    });
});
const ratingOptions = document.querySelectorAll('.rating-option');
    
    ratingOptions.forEach(option => {
        option.addEventListener('click', function() {
            // Enlever la sélection de tous les autres
            ratingOptions.forEach(opt => opt.classList.remove('selected'));
            
            // Ajouter la sélection à celui cliqué
            this.classList.add('selected');
            
            // Cocher le radio button correspondant
            const radioInput = this.querySelector('input[type="radio"]');
            if (radioInput) {
                radioInput.checked = true;
            }
        });
    });