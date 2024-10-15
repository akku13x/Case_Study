import sys
import os

# Get the absolute path of the root project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.Incidents import Incidents
from entity.Reports import Reports
from entity.Cases import Cases
from entity.Evidence import Evidence
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from datetime import datetime

class Main_menu:
     crime_analysis_service_impl = CrimeAnalysisServiceImpl()
     def main_menu(self):
          print("\n\t\t!!! Welcome to Crime Analysis and Reporting System !!!")
          while True:
               print(
                    """      
                    1. Create a new incident
                    2. Update the status of an incident 
                    3. Get a list of incidents within a date range
                    4. Search for incidents based on incident type 
                    5. Create report on an incident 
                    6. Create a new case 
                    7. Get details of a specific case 
                    8. Update case details
                    9. List of all Cases
                    10. Insert Evidence
                    0. Exit
                    """
               )
               choice = int(input("Please choose from the above options: "))

               if choice == 1:
                    IncidentID = int(input("Enter Incident ID: "))
                    IncidentType = input("Enter Incident Type: ")
                    IncidentDate = datetime.strptime(input("Enter Incident Date (DD-MM-YYYY): "), '%d-%m-%Y')
                    Location_Longitude = float(input("Enter Location Longitude: "))
                    Location_Latitude = float(input("Enter Location Latitude: "))
                    Description = input("Enter Incident Description: ")
                    Status = input("Enter Incident Status: ")
                    VictimID = int(input("Enter Victim ID: "))
                    SuspectID = int(input("Enter Suspect ID: "))
                    newIncident = Incidents(IncidentID, IncidentType, IncidentDate, Location_Longitude, Location_Latitude, Description, Status, VictimID, SuspectID)
                    self.crime_analysis_service_impl.createIncident(newIncident)
               if choice == 2:
                    IncidentID = int(input("Enter Incident ID: "))
                    Status = input("Enter Incident Status: ")
                    self.crime_analysis_service_impl.updateIncidentStatus(Status, IncidentID)
               if choice == 3:
                    startDate = datetime.strptime(input("Enter Start Date (DD-MM-YYYY): "), '%d-%m-%Y')
                    endDate = datetime.strptime(input("Enter End Date (DD-MM-YYYY): "), '%d-%m-%Y')
                    self.crime_analysis_service_impl.getIncidentsInDateRange(startDate, endDate)
               if choice == 4:
                    IncidentType = input("Enter Incident Type: ")
                    self.crime_analysis_service_impl.searchIncidents(IncidentType)
               if choice == 5:
                    ReportID = int(input("Enter Report ID: "))
                    IncidentID = int(input("Enter Incident ID: "))
                    ReportingOfficerID = int(input("Enter Reporting Officer ID: "))
                    ReportDate = datetime.strptime(input("Enter Report Date (DD-MM-YYYY): "), '%d-%m-%Y')
                    ReportDetails = input("Enter Report Details: ")
                    Status = input("Enter Report Status: ")
                    newReports = Reports(ReportID, IncidentID, ReportingOfficerID, ReportDate, ReportDetails, Status)
                    self.crime_analysis_service_impl.generateIncidentReport(newReports)
               if choice == 6:
                    CaseID = int(input("Enter Case ID: "))
                    IncidentID = int(input("Enter Incident ID: "))
                    Details = input("Enter Case Details: ")
                    newCases = Cases(CaseID, IncidentID, Details)
                    self.crime_analysis_service_impl.createCase(newCases)
               if choice == 7:
                    CaseID = int(input("Enter Case ID: "))
                    self.crime_analysis_service_impl.getCaseDetails(CaseID)
               if choice == 8:
                    CaseID = int(input("Enter Case ID: "))
                    Details = input("Enter Case Details: ")
                    self.crime_analysis_service_impl.updateCaseDetails(CaseID, Details)
               if choice == 9:
                    self.crime_analysis_service_impl.getAllCases()
               # if choice == 10:
               #      EvidenceID = int(input("Enter EvidenceID"))
               #      Description = input("Enter description")
               #      LocationFound = input("Location of evidence")
               #      IncidentID = int(input("Enter the incident id"))
               #      newEvidence = Evidence(EvidenceID, Description, LocationFound, IncidentID)
               #      self.crime_analysis_service_impl.registerev(newEvidence)

               if choice == 0:
                    self.crime_analysis_service_impl.close()
                    print("\n\t\t!!! You are now exiting the system !!!")
                    break

def main():
     mainMenu = Main_menu()
     mainMenu.main_menu()

if __name__ == '__main__':
     main()