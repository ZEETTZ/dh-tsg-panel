$(function() {
    let isDragging = false;

    // 初始化显示第一个表单的内容
    $('.collapsible-form:first-child .form-body').show();

    // 从 localStorage 中恢复表单状态
    $('.collapsible-form').each(function() {
        const formBody = $(this).find('.form-body');
        const formId = $(this).attr('id');
        const isVisible = localStorage.getItem(formId + 'Visibility') === 'true';
        formBody.toggle(isVisible);
    });

    // 处理点击事件
    $('.collapsible-form .form-header').on('click', function() {
        if (isDragging) return; // 如果正在拖动，则忽略点击事件

        const $formBody = $(this).next('.form-body');
        $formBody.slideToggle(function() {
            const formId = $(this).closest('.collapsible-form').attr('id');
            const isVisible = $formBody.is(':visible');
            localStorage.setItem(formId + 'Visibility', isVisible);
        });
    });

    // 设置表单位置
    const forms = $('form.collapsible-form');
    const numForms = forms.length;
    const screenWidth = $(window).width();
    const screenHeight = $(window).height();
    const formWidth = forms.first().outerWidth();
    const formHeight = forms.first().outerHeight();
    const horizontalSpacing = (screenWidth - (numForms * formWidth)) / (numForms + 1);

    for (let i = 0; i < numForms; i++) {
        const formId = forms.eq(i).attr('id');
        const leftPos = horizontalSpacing + (horizontalSpacing + formWidth) * i;
        const topPos = (screenHeight - formHeight) / 2;
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

    // 使表单可拖动
    forms.draggable({
        containment: 'window',
        handle: '.drag-handle', // 指定拖动句柄
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