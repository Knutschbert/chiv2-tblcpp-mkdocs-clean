---
title: UTBLAILibrary
type: class
aliases: UTBLAILibrary
share: false

---

# UTBLAILibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AITagActor]]**(AActor * Actor, FGameplayTagContainer TagsToAdd, EFaction Faction, bool bUntagWhenActorDies) |
| void | **[[AITagManyActors]]**(TArray< AActor * > Actors, FGameplayTagContainer TagsToAdd, EFaction Faction, bool bUntagWhenActorDies) |
| void | **[[AIUntagActor]]**(AActor * Actor, FGameplayTagContainer TagsToRemove, EFaction Faction) |
| void | **[[AIUntagAllActorsForFaction]]**(UObject * WorldContextObject, FGameplayTagContainer TagsToRemove, EFaction Faction) |
| void | **[[AIUntagManyActors]]**(TArray< AActor * > Actor, FGameplayTagContainer TagsToRemove, EFaction Faction) |
| void | **[[ClearAllAITagsForFaction]]**(UObject * WorldContextObject, EFaction Faction) |
| void | **[[CreateAvoidanceArea]]**(UObject * WorldContextObject, UObject * Instigator, const FVector & Location, float Radius) |
| FGameplayTagContainer | **[[GetActorAITags]]**(AActor * Actor, EFaction Faction) |
| TSet< AActor * > | **[[GetActorsByAITag]]**(UObject * WorldContextObject, FGameplayTag Tag, EFaction Faction) |
| bool | **[[GetPerceivedLocationOfActor]]**(AAIController * Controller, AActor * Actor, FVector & OutVector) |
| float | **[[InfluenceAtLocation]]**(TSubclassOf< [UI_Influence](/docs/SDK/Source/Classes/classUI__Influence.md) > InfluenceInput, AAIController * Controller, FVector Location) |
| void | **[[PlayEmote]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FName EmoteName) |
| void | **[[RemoveAvoidanceArea]]**(UObject * WorldContextObject, UObject * Instigator) |
| [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) * | **[[SpawnTBLAIControllerFromClass]]**(UObject * WorldContextObject, EFaction Faction, TSubclassOf< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) > ControllerClass, TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > NextSpawnCharacterClass, UBehaviorTree * BehaviorTree, bool IsPlayerBot) |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[SpawnTBLAIFromClass]]**(UObject * WorldContextObject, TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > CharacterClass, EFaction Faction, TSubclassOf< [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md) > ControllerClass, UBehaviorTree * BehaviorTree, FVector Location, FRotator Rotation, bool bNoCollisionFail) |
| | **[[UTBLAILibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200