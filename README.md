# Maximo IFIX Release Notifier

This script periodically checks for new Maximo IFIX releases and sends an email notification to the specified recipient when a new release is detected. The script reads the existing and latest IFIX releases from an Excel spreadsheet, compares them, and notifies the recipient if a new release is found.

To run the script manually, simply run the `scheduled_script.py` file. To schedule the script to run periodically using the Windows Task Scheduler, follow these instructions:

1. Open Windows Task Scheduler.
2. Click on `Create Task`.
3. Give the task a name and description. 
4. Under the `Triggers` tab, click on `New` and choose how often the task should run (e.g., daily or weekly).
5. Under the `Actions` tab, click on `New` and enter the path to the path to the `scheduled_script.py` file. 
6. Under the `Conditions` tab, select any additional conditions for when the task should run (e.g., if the computer is idle). 
7. Click `OK` to save the task.

**Note**: Remember to set the correct paths to `scheduled_script.py` file in step 5. 
