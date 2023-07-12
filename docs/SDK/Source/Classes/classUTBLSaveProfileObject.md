---
title: UTBLSaveProfileObject
type: class
aliases: UTBLSaveProfileObject
share: false

---

# UTBLSaveProfileObject





Inherits from USaveGame

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UTBLSaveProfileObject]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FTBLCampaignSettings](/docs/SDK/Source/Classes/structFTBLCampaignSettings.md) | **[[CampaignSettings]]**  |
| [FTBLConsoleSaveSettings](/docs/SDK/Source/Classes/structFTBLConsoleSaveSettings.md) | **[[ConsoleUserSettings]]**  |
| [FTBLCustomizationSaveSettings](/docs/SDK/Source/Classes/structFTBLCustomizationSaveSettings.md) | **[[CustomizationSettings]]**  |
| TMap< FString, int32 > | **[[FlavorStats]]**  |
| [FTBLGameUpdateSettings](/docs/SDK/Source/Classes/structFTBLGameUpdateSettings.md) | **[[GameUpdateSettings]]**  |
| FDateTime | **[[LastReadDeveloperMessageTime]]**  |
| TArray< FPrimaryAssetId > | **[[ViewedItems]]**  |
| bool | **[[bFirstLoadCompleted]]**  |
| bool | **[[bHasAgreedToTOS]]**  |
| bool | **[[bPlayerHasAcceptedNDA]]**  |
| bool | **[[bPlayerHasAcceptedPurchaseDisclaimer]]**  |
| bool | **[[bPlayerHasPlayedTutorial]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< FString, double > | **[[AchievementProgress]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200