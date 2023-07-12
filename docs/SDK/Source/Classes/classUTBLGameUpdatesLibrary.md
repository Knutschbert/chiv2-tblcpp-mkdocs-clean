---
title: UTBLGameUpdatesLibrary
type: class
aliases: UTBLGameUpdatesLibrary
share: false

---

# UTBLGameUpdatesLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[GetGameUpdateData]]**(FName UpdateVersion, [FGameUpdateData](/docs/SDK/Source/Classes/structFGameUpdateData.md) & OutGameUpdateData, UObject * WorldContextObject) |
| void | **[[GetGameUpdates]]**(TArray< [FGameUpdateData](/docs/SDK/Source/Classes/structFGameUpdateData.md) > & OutGameUpdates, UObject * WorldContextObject, uint8 Count) |
| bool | **[[GetHasUnseenGameUpdates]]**(UObject * WorldContextObject) |
| bool | **[[GetIsGameUpdateActive]]**(const [FGameUpdateData](/docs/SDK/Source/Classes/structFGameUpdateData.md) & GameUpdateData) |
| bool | **[[GetIsGameUpdateNewest]]**(const [FGameUpdateData](/docs/SDK/Source/Classes/structFGameUpdateData.md) & GameUpdateData, UObject * WorldContextObject, bool ShouldCheckIfSeen) |
| bool | **[[GetIsGameUpdateSeen]]**(const FString & UpdateVersion, UObject * WorldContextObject) |
| bool | **[[GetNewestGameUpdate]]**([FGameUpdateData](/docs/SDK/Source/Classes/structFGameUpdateData.md) & OutGameUpdateData, UObject * WorldContextObject, bool ShouldCheckIfSeen) |
| int32 | **[[GetUnseenGameUpdatesCount]]**(UObject * WorldContextObject) |
| void | **[[SetIsGameUpdateSeen]]**(const FString & UpdateVersion, UObject * WorldContextObject, bool IsSeen) |
| bool | **[[ShouldShowGameUpdate]]**(const [FGameUpdateData](/docs/SDK/Source/Classes/structFGameUpdateData.md) & GameUpdateData) |
| | **[[UTBLGameUpdatesLibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200