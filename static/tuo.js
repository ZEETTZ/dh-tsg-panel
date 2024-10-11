$(function() {
    let isDragging = false;


    $('.collapsible-form:first-child .form-body').show();


    $('.collapsible-form').each(function() {
        const formBody = $(this).find('.form-body');
        const formId = $(this).attr('id');
        const isVisible = localStorage.getItem(formId + 'Visibility') === 'true';
        formBody.toggle(isVisible);
    });


    $('.collapsible-form .form-header').on('click', function() {
        if (isDragging) return; 

        const $formBody = $(this).next('.form-body');
        $formBody.slideToggle(function() {
            const formId = $(this).closest('.collapsible-form').attr('id');
            const isVisible = $formBody.is(':visible');
            localStorage.setItem(formId + 'Visibility', isVisible);
            
        });
    });


    const forms = $('form.collapsible-form');
    const numForms = forms.length;
    const screenWidth = $(window).width();
    const screenHeight = $(window).height();
    const defaultPositions = {
        form1: {top: 22.000003814697266, left: 1299.157470703125},
        form2: {top: 31.7906494140625, left: 59.86993408203125},
        form3: {top: 431.9125061035156, left: 59.350006103515625},
        form4: {top: 146, left: 1299.4781494140625},
        form5: {top: 15.787506103515625, left: 456.95001220703125}
    };

    for (let i = 0; i < numForms; i++) {
        const formId = forms.eq(i).attr('id');
        const defaultPosition = defaultPositions[formId];
        const leftPos = defaultPosition ? defaultPosition.left : (screenWidth - forms.first().outerWidth()) / 2;
        const topPos = defaultPosition ? defaultPosition.top : (screenHeight - forms.first().outerHeight()) / 2;

        forms.eq(i).css({
            left: leftPos + 'px',
            top: topPos + 'px'
        });

        if (localStorage.getItem(formId + 'Position')) {
            const position = JSON.parse(localStorage.getItem(formId + 'Position'));
            forms.eq(i).css({
                left: position.left + 'px',
                top: position.top + 'px'
            });
        }
    }


    forms.draggable({
        containment: 'window',
        handle: '.drag-handle', 
        start: function() {
            isDragging = true;
        },
        stop: function(event, ui) {
            isDragging = false;
            const formId = $(this).closest('.collapsible-form').attr('id');
            if (formId) {
                localStorage.setItem(formId + 'Position', JSON.stringify(ui.position));
            }
        }
    });
});