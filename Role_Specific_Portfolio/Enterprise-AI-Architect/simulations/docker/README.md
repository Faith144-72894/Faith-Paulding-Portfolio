# Docker — Container deployment

Original interactive configuration simulation. Download index.html and open locally in a browser. GitHub file preview does not execute HTML. This is not a replica of the vendor interface; settings are illustrative and must be verified in a real sandbox.

[Interactive HTML source](index.html)

## 01 — Base image
![Simulated configuration](screens/01.svg)
Select **Base image** in the simulation navigation, enter `Python runtime`, then select **Save simulated setting**. Confirm the configuration record contains the value before selecting Next step. This verifies local state only.

## 02 — Workdir
![Simulated configuration](screens/02.svg)
Select **Workdir** in the simulation navigation, enter `/app`, then select **Save simulated setting**. Confirm the configuration record contains the value before selecting Next step. This verifies local state only.

## 03 — Dependencies
![Simulated configuration](screens/03.svg)
Select **Dependencies** in the simulation navigation, enter `requirements.txt`, then select **Save simulated setting**. Confirm the configuration record contains the value before selecting Next step. This verifies local state only.

## 04 — Port
![Simulated configuration](screens/04.svg)
Select **Port** in the simulation navigation, enter `8000`, then select **Save simulated setting**. Confirm the configuration record contains the value before selecting Next step. This verifies local state only.

## 05 — Build
![Simulated configuration](screens/05.svg)
Select **Build** in the simulation navigation, enter `portfolio-api`, then select **Save simulated setting**. Confirm the configuration record contains the value before selecting Next step. This verifies local state only.

## 06 — Run
![Simulated configuration](screens/06.svg)
Select **Run** in the simulation navigation, enter `Local container`, then select **Save simulated setting**. Confirm the configuration record contains the value before selecting Next step. This verifies local state only.

## 07 — Test
![Simulated configuration](screens/07.svg)
Select **Test** in the simulation navigation, enter `/health`, then select **Save simulated setting**. Confirm the configuration record contains the value before selecting Next step. This verifies local state only.

