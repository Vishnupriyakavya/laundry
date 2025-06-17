// Custom Admin JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Add status classes to active/inactive fields
    const statusFields = document.querySelectorAll('.field-is_active');
    statusFields.forEach(field => {
        const value = field.textContent.trim();
        if (value === 'True') {
            field.classList.add('status-active');
        } else {
            field.classList.add('status-inactive');
        }
    });

    // Enhance image previews
    const imagePreviews = document.querySelectorAll('.field-image img');
    imagePreviews.forEach(img => {
        img.classList.add('image-preview');
    });

    // Add tooltips to action buttons
    const actionButtons = document.querySelectorAll('.button');
    actionButtons.forEach(button => {
        const title = button.getAttribute('title') || button.textContent;
        button.setAttribute('data-tooltip', title);
    });

    // Enhance form field focus
    const formFields = document.querySelectorAll('input, select, textarea');
    formFields.forEach(field => {
        field.addEventListener('focus', function() {
            this.parentElement.classList.add('field-focused');
        });
        field.addEventListener('blur', function() {
            this.parentElement.classList.remove('field-focused');
        });
    });

    // Add confirmation to delete actions
    const deleteButtons = document.querySelectorAll('.deletelink');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Enhance filter sidebar
    const filterSidebar = document.querySelector('#changelist-filter');
    if (filterSidebar) {
        const filterLinks = filterSidebar.querySelectorAll('a');
        filterLinks.forEach(link => {
            link.addEventListener('click', function() {
                filterLinks.forEach(l => l.classList.remove('selected'));
                this.classList.add('selected');
            });
        });
    }

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + S to save
        if ((e.ctrlKey || e.metaKey) && e.key === 's') {
            e.preventDefault();
            const saveButton = document.querySelector('input[name="_save"]');
            if (saveButton) saveButton.click();
        }
    });

    // Enhance search field
    const searchField = document.querySelector('#searchbar');
    if (searchField) {
        searchField.setAttribute('placeholder', 'Search...');
        searchField.addEventListener('focus', function() {
            this.parentElement.classList.add('search-focused');
        });
        searchField.addEventListener('blur', function() {
            this.parentElement.classList.remove('search-focused');
        });
    }

    // Add loading indicators
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('input[type="submit"]');
            if (submitButton) {
                submitButton.value = 'Saving...';
                submitButton.disabled = true;
            }
        });
    });
}); 