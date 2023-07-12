---
title: UGameConfigObjectBase
type: class
aliases: UGameConfigObjectBase
share: false

---

# UGameConfigObjectBase





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UGameConfigObjectBase]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BuildDerivedProperties]]**() |
| void | **[[CacheAllMapsData]]**(const TArray< [FMapOption](/docs/SDK/Source/Classes/structFMapOption.md) > & MapOptions, bool bClearOldData) |
| void | **[[CacheMapData]]**(const [FMapOption](/docs/SDK/Source/Classes/structFMapOption.md) & MapOption) |
| void | **[[ClearCachedMapsData]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< FString, [FMapSummaryData](/docs/SDK/Source/Classes/structFMapSummaryData.md) > | **[[MapSummaryLookup]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200