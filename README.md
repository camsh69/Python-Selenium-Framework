# Python-Selenium-Framework

`cd` into tests folder to run tests - this ensures report.html, screenshots and logfiles are generated within tests folder

`python --html=report.html` to generate a report,
`python --browser_name=chrome` to run a particular browser (firefox and edge also configured)
Also `-v` for verbose, `-s` for added info and `-q` for quiet

Run Jenkins from **cmd** `java -jar jenkins.war` and open 'http://localhost:8080'.
Reports run from Jenkins configured to output to separate reports folder - issue is screenshots aren't attached. See To Do.

**NB** Environment variables have been changed to point to Java 11 as 17 not supported by Jenkins.

To Do: Figure out how to either generate report and screenshot in a different folder or move to a different folder once generated.
