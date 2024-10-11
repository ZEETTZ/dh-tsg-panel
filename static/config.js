function validateInput(inputId, maxValue) {
    const input = document.getElementById(inputId);
    input.addEventListener('input', function(event) {
        const inputValue = parseFloat(event.target.value);
        if (inputValue > maxValue) {
            alert(`输入值不能超过 ${maxValue}`);
            event.target.value = maxValue; // 将值重置为最大值
        }
    });
}

window.onload = function() {
    validateInput('playermax', 64);
    validateInput('thralls', 64);
    validateInput('dayminutes', 15);
    validateInput('daysbeforeblizzard', 6);
    validateInput('predatordamage', 3);
    validateInput('coalburnrate', 3);
    validateInput('hungerrate', 3);
    validateInput('coldintensity', 3);
};


document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.delete-button').forEach(button => {
        button.addEventListener('click', function(event) {
            const filename = this.closest('tr').querySelector('td:nth-child(2)').textContent;
            deleteFile(filename, this); 
        });
    });

    function deleteFile(filename, button) {
        fetch(`/delete?filename=${encodeURIComponent(filename)}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const row = button.closest('tr');
                row.parentNode.removeChild(row);
                location.reload();
            } else {
                alert('删除失败: ' + data.message);
            }
        })
    }
});

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.edit-button').forEach(button => {
        button.addEventListener('click', function(event) {
            const filename = this.closest('tr').querySelector('td:nth-child(2)').textContent;
            editFile(filename, this); 
        });
    });




    function editFile(filename) {
        window.location.href = `/edit?filename=${encodeURIComponent(filename)}`;
    }

});

//移动
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.move-button').forEach(button => {
        button.addEventListener('click', function(event) {
            const filename = this.closest('tr').querySelector('td:nth-child(2)').textContent;
            editFileBin(filename, this); 
        });
    });




    function editFileBin(filename) {
        window.location.href = `/move?filename=${encodeURIComponent(filename)}&next=/config`;
    }

});

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.editbin-button').forEach(button => {
        button.addEventListener('click', function(event) {
            const filename = this.closest('tr').querySelector('td:nth-child(2)').textContent;
            editFileBin(filename, this); 
        });
    });




    function editFileBin(filename) {
        window.location.href = `/editbin?filename=${encodeURIComponent(filename)}`;
    }

});



function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert("请选择一个文件");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(data.message);
            // 页面刷新
            location.reload();
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
