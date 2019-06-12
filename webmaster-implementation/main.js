// Warning: the if-statement determines if the user has opted out of Annie data collection or not
// Removing it is in violation of our ToS
if(!document.cookie.split("; ")[0] == "annie_optout=yes") {
  new XMLHttpRequest().open("GET", "https://api.annieapp.co/ping?dataset=YOUR_PUBLIC_KEY", true).send();
}
