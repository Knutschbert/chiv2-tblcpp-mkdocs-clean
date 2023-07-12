---
title: UTBLTitleScreen
type: class
aliases: UTBLTitleScreen
share: false

---

# UTBLTitleScreen





Inherits from [UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md), [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md), UUserWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[Logout]]**() |
| void | **[[RetryMaintenance]]**() |
| | **[[UTBLTitleScreen]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[K2_OnStateChanged]]**(ETitleScreenMode NewState) |
| void | **[[OnMaintenanceDataLoaded]]**() |
| void | **[[OnPlayTutorialAccepted]]**() |
| void | **[[OnPlayTutorialDeclined]]**() |
| void | **[[OnTOSAgreed]]**() |
| void | **[[OnTOSDeclined]]**() |
| void | **[[OnUserPressedLogin]]**(int32 ControllerIndex, const FString & InEGSDevAuth_Address, const FString & InEGSDevAuth_Client) |
| void | **[[OnUserPressedOfflineMode]]**(int32 ControllerIndex) |
| void | **[[OnUserPressedStart]]**(int32 ControllerIndex) |
| bool | **[[ShouldShowEgsDevLoginCredentials]]**() const |
| bool | **[[ShouldUsePCStyleWelcomeScreen]]**() const |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FString | **[[EGSDevAuth_Address]]**  |
| FString | **[[EGSDevAuth_Client]]**  |
| FText | **[[ErrorMessageBody]]**  |
| FText | **[[ErrorMessageTitle]]**  |
| FDateTime | **[[MaintenanceCurrentTime]]**  |
| FDateTime | **[[MaintenanceEndTime]]**  |
| ETitleScreenMode | **[[State]]**  |
| bool | **[[bSavedHasAgreedToTOS]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200