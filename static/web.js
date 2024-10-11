function updateProcessStatus() {
    fetch('/process_status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('process-status').textContent = data.exists ? '存在' : '不存在';
        });
}


function updatePortStatus() {
    fetch('/port')
        .then(response => response.json())
        .then(data => {
            if ('port' in data) { // 确认数据中存在'port'字段
                document.getElementById('port').textContent = `${data.port}`;
            } else {
                console.error("Invalid data format from server");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


function updateConsole() {
    fetch('/get_logs')
        .then(response => response.text())
        .then(data => {
            document.getElementById('console-output').textContent = data;
        });
}

window.onload = function() {
    updateConsole();
    updateProcessStatus();
    updatePortStatus();
    setInterval(updateProcessStatus, 3000); 
    setInterval(updatePortStatus, 3000);
    setInterval(updateConsole, 1000);
};

document.addEventListener('DOMContentLoaded', function() {
    var checkboxes = document.getElementsByName('serverOption');
    
    for (var i = 0; i < checkboxes.length; i++) {
        var checkbox = checkboxes[i];
        
        if (localStorage.getItem(checkbox.name)) {
            checkbox.checked = localStorage.getItem(checkbox.name) === 'true';
        }
        
        checkbox.addEventListener('change', function(event) {
            localStorage.setItem(this.name, this.checked);
        });
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const startServerLink = document.querySelector('a[href="/start_server"]');
    const autoRestartCheckbox = document.getElementById('autoRestartCheckbox');
    updateStartServerLink(autoRestartCheckbox.checked);
    autoRestartCheckbox.addEventListener('change', function() {
        updateStartServerLink(this.checked);
    });
    function updateStartServerLink(shouldAutoRestart) {
        if (shouldAutoRestart) {
            startServerLink.href = "/start_server/auto";
        } else {
            startServerLink.href = "/start_server";
        }
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const startServerLink = document.querySelector('a[href="/stop_server"]');
    const autoRestartCheckbox = document.getElementById('autoRestartCheckbox');
    updateStartServerLink(autoRestartCheckbox.checked);
    autoRestartCheckbox.addEventListener('change', function() {
        updateStartServerLink(this.checked);
    });
    function updateStartServerLink(shouldAutoRestart) {
        if (shouldAutoRestart) {
            startServerLink.href = "/stop_server/auto";
        } else {
            startServerLink.href = "/stop_server";
        }
    }
});




