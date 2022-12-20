# is_rockets_down
Send email if the website https://clubrockets.com/ or https://clubrockets.ca/  is down.


# Note pour me rappeler de ce que j'ai fait
Ajout d'une job cron sur un raspberry pi qui appel un script python afin de me notifier lorsque l'un des sites du club rockets est down.

Pour ajouter une nouvelle job cron il suffit d'ajout le path de python + le path du script :

```crontab -e ```

```*/5 * * * * /usr/bin/python3 /home/docanimo/is_rockets_down/is_rockets_down.py```

Ceci va appeler le script à chaque 5 minutes.
