---
title: UTBLAISystem
type: class
aliases: UTBLAISystem
share: false

---

# UTBLAISystem





Inherits from UAISystem

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CreateAvoidanceArea]]**(UObject * Instigator, const FVector & Location, float Radius) |
| TSet< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * > | **[[GetControllersTargetting]]**(AActor * Target) const |
| TSet< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * > | **[[GetControllersTargettingLocation]]**(const FVector & TargetLocation) const |
| TSet< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * > | **[[GetControllersWithBehaviour]]**(TSubclassOf< [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) > Behaviour) const |
| TSet< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * > | **[[GetControllersWithWeapon]]**(TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > Weapon) const |
| int32 | **[[GetNumControllersRegistered]]**(EFaction Faction) const |
| int32 | **[[GetNumControllersTargetting]]**(AActor * Target) const |
| int32 | **[[GetNumControllersTargettingLocation]]**(const FVector & TargetLocation) const |
| int32 | **[[GetNumControllersWithBehaviour]]**(TSubclassOf< [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) > Behaviour) const |
| int32 | **[[GetNumControllersWithWeapon]]**(TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > Weapon) const |
| float | **[[GetObjectiveTimePercentRemaining]]**() const |
| float | **[[GetObjectiveTimeRemaining]]**() const |
| FVector | **[[GetSpawnCenter]]**(EFaction Faction) |
| void | **[[NotifyControllerTarget]]**([ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * Controller, AActor * NewTarget) |
| void | **[[NotifyControllerTargetLocation]]**([ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * Controller, const FVector & NewTargetLocation) |
| void | **[[OnPlayerPossessed]]**(AController * Controller, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[RemoveAvoidanceArea]]**(UObject * Instigator) |
| | **[[UTBLAISystem]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< TSubclassOf< [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) >, [FControllerArray](/docs/SDK/Source/Classes/structFControllerArray.md) > | **[[BehaviourMap]]**  |
| TArray< FString > | **[[BotNames]]**  |
| TSet< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * > | **[[BotsWithSpecialNames]]**  |
| TMap< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) *, TSubclassOf< [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) > > | **[[ControllerBehaviourMap]]**  |
| TMap< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) *, FVector > | **[[ControllerLocationMap]]**  |
| TMap< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) *, [FWeaponClassSet](/docs/SDK/Source/Classes/structFWeaponClassSet.md) > | **[[ControllerWeaponMap]]**  |
| TMap< AActor *, [FControllerArray](/docs/SDK/Source/Classes/structFControllerArray.md) > | **[[CurrentTargeters]]**  |
| TMap< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) *, AActor * > | **[[CurrentTargets]]**  |
| TMap< FVector, [FControllerArray](/docs/SDK/Source/Classes/structFControllerArray.md) > | **[[LocationMap]]**  |
| [UAITagSystem](/docs/SDK/Source/Classes/classUAITagSystem.md) * | **[[TagSystem]]**  |
| TMap< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) >, [FControllerArray](/docs/SDK/Source/Classes/structFControllerArray.md) > | **[[WeaponMap]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200