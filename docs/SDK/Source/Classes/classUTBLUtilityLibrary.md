---
title: UTBLUtilityLibrary
type: class
aliases: UTBLUtilityLibrary
share: false

---

# UTBLUtilityLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CopyToClipboard]]**(const FString & TextToCopy) |
| FName | **[[FindClosestSocket]]**(USceneComponent * Component, FVector Location, const FString & SocketSubstring) |
| float | **[[GetAzimuth]]**(const FVector & Direction, const FVector & Forward) |
| float | **[[GetClosestPointOnCollision]]**(const AActor * Actor, const FVector & Point, TEnumAsByte< ECollisionChannel > CollisionChannel, FVector & ClosestPointOnCollision) |
| void | **[[GetMatchingChildComponentsByName]]**(const USceneComponent * RootComponent, const FString & MatchName, TArray< USceneComponent * > & OutMatches) |
| TEnumAsByte< EPlatformType > | **[[GetPlatformType]]**() |
| TArray< [FSwatchSelectionsByClass](/docs/SDK/Source/Classes/structFSwatchSelectionsByClass.md) > | **[[GetSavedCustomizationSettings]]**() |
| TEnumAsByte< ESonyAppType > | **[[GetSonyPlatformRegion]]**() |
| void | **[[LoadCinematicSublevel]]**(const UObject * WorldContextObject, FName LevelName, bool bMakeVisibleAfterLoad, bool bShouldBlockOnLoad, FLatentActionInfo LatentInfo) |
| void | **[[LogWithCallstacks]]**(const FString & Message) |
| int32 | **[[RandomWeightedIntegerFromStream]]**(const TArray< float > & Weights, const FRandomStream & InStream) |
| void | **[[RecursiveSetVisibility]]**(UPrimitiveComponent * Root, bool bOwnerNoSee, bool bOnlyOwnerSee) |
| void | **[[SaveCustomizationSettings]]**() |
| void | **[[SetAudioEnemyRTPC]]**(UAkComponent * AkComponent, AActor * Initiator) |
| void | **[[SetEnabledRenderMainScene]]**(UObject * WorldContextObject, bool bShouldRenderMainScene) |
| | **[[UTBLUtilityLibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200