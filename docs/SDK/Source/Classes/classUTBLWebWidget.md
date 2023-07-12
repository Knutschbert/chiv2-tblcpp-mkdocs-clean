---
title: UTBLWebWidget
type: class
aliases: UTBLWebWidget
share: false

---

# UTBLWebWidget





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BrowseToUrl]]**(const FString & URL) |
| void | **[[ClickedButton]]**(int32 ButtonIndex) |
| FString | **[[GetButtonText]]**(int32 ButtonIndex) |
| void | **[[InitializeWidget]]**() |
| | **[[UTBLWebWidget]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FColor | **[[BackgroundColor]]**  |
| FString | **[[InitialURL]]**  |
| FOnBeforeBrowseDynamic | **[[OnBeforeNavigationEvent]]**  |
| FSimpleDelegateDynamic | **[[OnLoadCompletedEvent]]**  |
| FOnLoadUrlDynamic | **[[OnLoadUrlEvent]]**  |
| FSimpleDelegateDynamic | **[[OnSourceParsedEvent]]**  |
| FOnTextChangedDynamic | **[[OnTitleChanged]]**  |
| FOnTextChangedDynamic | **[[OnUrlChanged]]**  |
| bool | **[[ShowAddressBar]]**  |
| bool | **[[ShowControls]]**  |
| bool | **[[ShowErrorMessage]]**  |
| bool | **[[ShowInitialThrobber]]**  |
| bool | **[[SupportsThumbMouseButtonNavigation]]**  |
| bool | **[[SupportsTransparency]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200