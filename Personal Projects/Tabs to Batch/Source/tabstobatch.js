/********************************
 * Tabs to Batch
 * tabstobatch.js
 * Created by Justin Leonard
********************************/

/**
* Get the urls of all open tabs in the current window.
*
* @param  {function(array of strings)} callback called when all urls are obtained
*/
function getUrls(callback) {
	// Variables
	var listOfUrls = [];
	
	// Get current tabs
	chrome.windows.getCurrent(function(win) {
		// Get all tabs in the window
		chrome.tabs.getAllInWindow(win.id, function(listOfTabs) {
			// Add urls to list
			for (var i = 0; i < listOfTabs.length; i++) {
				listOfUrls.push(listOfTabs[i].url);
			}

			// Callback
			callback(listOfUrls);
		});
	});
}

/**
* Save the urls of the current tabs to a batch file.
*
* @param  urls the list of urls
*/
function saveBatchFile(urls) {
		// Variables
		var stringExec = "";
		var stringUrl = "";
		var stringNewWindow = "";
		var stringIncognito = "";
		var stringFinal = "";

		// Set url
		for (var i = 0; i < urls.length; i++) {
			if (!urls[i].includes("chrome://")) {
				stringUrl = stringUrl + "\"" + urls[i] + "\" ";
			} else {
				stringUrl = stringUrl + "\"https://www.google.com/\" ";
			}
		}

		// Check new window
		if (document.getElementById("checkboxNewWindow").checked) {
			stringNewWindow = "--new-window ";
		} else {
			stringNewWindow = "";
		}

		// Check incognito
		if (document.getElementById("checkboxIncognito").checked) {
			stringIncognito = "--incognito ";
		} else {
			stringIncognito = "";
		}

		// Set strings
		stringExec = "@echo off\r\ncd \"%ProgramFiles(x86)%\\Google\\Chrome\\Application\"\r\nchrome " + stringNewWindow + stringIncognito;
		stringFinal = stringExec + stringUrl;

		// Variables
		var saveFileDialog = document.createElement("a");
		var saveFileRaw = new Blob([stringFinal]);
		var saveFileContents = URL.createObjectURL(saveFileRaw);

		// Save file
		saveFileDialog.setAttribute("href", saveFileContents);
		saveFileDialog.setAttribute("download", "file.bat");
		saveFileDialog.click();
}

/**
* Chrome extension loaded.
*/
document.addEventListener('DOMContentLoaded', function() {
	/**
	* Save button click event.
	*/
	document.getElementById("buttonSave").addEventListener("click", function() {
		getUrls(saveBatchFile);
	});
});