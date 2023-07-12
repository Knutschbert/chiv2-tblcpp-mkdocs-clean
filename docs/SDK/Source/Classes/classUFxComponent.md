---
title: UFxComponent
type: class
aliases: UFxComponent
share: false

---

# UFxComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [UFxComponent](/docs/SDK/Source/Classes/classUFxComponent.md) * | **[[GetFXComponent]]**(AActor * Actor) |
| [UFxInstance](/docs/SDK/Source/Classes/classUFxInstance.md) * | **[[GetFXInstanceFromActor]]**(AActor * Actor, UClass * Blueprint, bool bCreateIfNeeded) |
| void | **[[PopMaterialOverride]]**() |
| void | **[[PushMaterialOverride]]**(UMaterialInterface * Material) |
| | **[[UFxComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FMaterialOverrideState](/docs/SDK/Source/Classes/structFMaterialOverrideState.md) | **[[MaterialOverrideState]]**  |
| TArray< TSubclassOf< [UFxInstance](/docs/SDK/Source/Classes/classUFxInstance.md) > > | **[[PersistentFXComponents]]**  |
| TArray< TSubclassOf< [UFxInstance](/docs/SDK/Source/Classes/classUFxInstance.md) > > | **[[PersistentFXComponentsForOwner]]**  |
| TArray< [UFxInstance](/docs/SDK/Source/Classes/classUFxInstance.md) * > | **[[PersistentFXInstances]]**  |
| TArray< UBlueprint * > | **[[PersistentFXs]]**  |
| TArray< UBlueprint * > | **[[PersistentFXsForOwner]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200