---
title: ATBLAICombatController
type: class
aliases: ATBLAICombatController
share: false

---

# ATBLAICombatController





Inherits from [ATBLAIController](/docs/SDK/Source/Classes/classATBLAIController.md), AAIController

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLAICombatController]]**() |
| void | **[[Attack]]**([FCombatAiAttackParams](/docs/SDK/Source/Classes/structFCombatAiAttackParams.md) InParams) |
| void | **[[Disengage]]**(const [FDisengageParams](/docs/SDK/Source/Classes/structFDisengageParams.md) & InDisengageParams) |
| void | **[[Dodge]]**(TArray< TEnumAsByte< EMovementDirection >> AllowedDirections) |
| void | **[[EnemyOnCombatStateBegin]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[Engage]]**(const [FEngageParams](/docs/SDK/Source/Classes/structFEngageParams.md) & InEngageParams) |
| EAiMeleeCombatMode | **[[GetMeleeCombatMode]]**() const |
| void | **[[HandleDamageCaused]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[HandleTookDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[HoldBlock]]**() |
| void | **[[OnCombatStateBegin]]**(AActor * Actor, FName State, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[ReleaseBlock]]**() |
| void | **[[StrafeAndKeepDistance]]**(EAiCombatDistance Distance, EAiCombatStrafing Strafing) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[Advantage]]**  |
| float | **[[AttackDistanceMultiplier]]**  |
| float | **[[AttackOkayMax]]**  |
| float | **[[CloseAttackRange]]**  |
| [UUtilityAI_CombatDecisionMaker](/docs/SDK/Source/Classes/classUUtilityAI__CombatDecisionMaker.md) * | **[[CombatDecisionMakerComponent]]**  |
| float | **[[CombatMovementMaxDistance]]**  |
| AActor * | **[[CombatTarget]]**  |
| float | **[[CombatTargetDesiredDistance]]**  |
| float | **[[CorneringDistance]]**  |
| float | **[[DefaultDistanceToKeep]]**  |
| EAiCombatDistance | **[[DesiredDistance]]**  |
| EAiCombatStrafing | **[[DesiredStrafing]]**  |
| float | **[[DisengagementMax]]**  |
| FTimerHandle | **[[EdgeDetectionTimer]]**  |
| float | **[[EngageSprintStartOkayMin]]**  |
| float | **[[EngageSprintStopMax]]**  |
| float | **[[EngagementMin]]**  |
| float | **[[FacehugRange]]**  |
| float | **[[FarAttackRange]]**  |
| float | **[[MediumAttackRange]]**  |
| EAiMeleeCombatMode | **[[MeleeCombatMode]]**  |
| FVector | **[[NearestNavWallNormal]]**  |
| float | **[[OffsetFromCornersDistance]]**  |
| float | **[[OutsideAttackRange]]**  |
| TArray< float > | **[[RecentBlockedHits]]**  |
| float | **[[SprintAttackOkayMax]]**  |
| float | **[[SprintAttackOkayMin]]**  |
| float | **[[StuckMaxTime]]**  |
| float | **[[TimeLastAttack]]**  |
| bool | **[[bSprinting]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200