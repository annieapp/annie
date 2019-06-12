if(!document.cookie.split("; ")[0] == "annie_optout=yes") new XMLHttpRequest().open("GET", "https://your-analytics-server-ip/ping", true).send();
