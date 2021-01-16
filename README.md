Hier findest du die Startseiten von https://www.opennet-initiative.de

Die Seite wird mit https://hugo.io erstellt und nutzt das Thema Syna (https://about.okkur.org/syna/).

Syna 0.17.4. benötigt mindestens Hugo 0.76.

## Installation

Siehe ansible ttp://dev.on-i.de/browser/on_ansible/roles/www-frontpage

## Einbindung Blogeinträge

Eine Anforderung an die Webseite war das Anzeigen der letzten Blogeinträge. Diese sollten ausschnittsweise auf der Seite angezeigt werden.

Wir betreiben derzeit (Stand Jan 2021) unser Blog unter https://stadtgestalten.org/opennet/. Hier gibt es auch einen RSS Feed.

Eine mögliche Einbindung der Blogeinträge könnte auf unterschiedliche Wege stattfinden. Hier wurden unterschiedliche Möglichkeiten getestet und sich für einen möglichst einfache Weg letztendlich entschieden. Ziel war es möglichst wenige Anpassungen an Software durchzuführen, sodass ein Update bestehender Software immer möglich ist. 

Der Ablauf hierfür ist folgender:
* Ein Python Skript [on-rss2md.py](on-rss2md.py) ermöglicht das Herunterladen des Stadtgestalten RSS Feeds und generiert daraus Markdown Text mit Auszügen der Blogeinträge.
* Ein Deployment Skript (on-hugo-deploy-prod.sh) :
  * schreibt das Ergebnis von on-rss2md.py in die Hugo Verzeichnisstruktur (dies wird später eingebunden von (content/_index/blog.md) )
  * generiert die Webseiten erneut
  * kopiert die neuen Dateien in das Apache www Verzeichnis
* Deployment Skript wird als Cronjob täglich gestartet



## Weitere Dokumentation

Es gibt weitere Dokumentation im Wiki unter https://wiki.opennet-initiative.de/wiki/Startseite_Webauftritt#Entwicklung

