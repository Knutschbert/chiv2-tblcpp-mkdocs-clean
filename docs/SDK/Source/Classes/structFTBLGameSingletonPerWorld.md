---
title: FTBLGameSingletonPerWorld
type: struct
aliases: FTBLGameSingletonPerWorld
share: false

---

# FTBLGameSingletonPerWorld





## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FTBLGameSingletonPerWorld]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< FName, [FActorArray](/docs/SDK/Source/Classes/structFActorArray.md) > | **[[ActorsByTag]]**  |
| TArray< [UCustomizationConfig](/docs/SDK/Source/Classes/classUCustomizationConfig.md) * > | **[[CustomizationConfigs]]**  |
| [FInventoryItemPool](/docs/SDK/Source/Classes/structFInventoryItemPool.md) | **[[InventoryItemPool]]**  |
| TSet< FName > | **[[LoadedCinematicSublevels]]**  |
| [UTextureAtlasManager](/docs/SDK/Source/Classes/classUTextureAtlasManager.md) * | **[[TextureAtlasManager]]**  |
| UWorld * | **[[World]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:02 +0200