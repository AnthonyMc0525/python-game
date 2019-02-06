class Job(object):

    def __init__(self, job_name):
        str_job_name = str(job_name)
        if str_job_name == 'black mage':
            fire = {'name': "fire", 'damage': 25, 'dmg_type': 'aoe'}
            blizzard = {'name': 'damage', 'damage': 50, 'dmg_type': 'single target'}
            leach = {'damage': 15, 'dmg_type': 'single_target', 'heal': 15}
            staff_attack = {'damage': 5, 'dmg_type': 'single_target'}
            class_skills = [fire, blizzard, leach, staff_attack]
            self.job_name = job_name
            self.hp_increase = 0
            self.str_increase = 0
            self.matk_increase = 3
            self.skills = class_skills

        elif str_job_name == 'paladin':
            holy_avenger = {'damage': 50, 'dmg_type': 'single_target'}
            guardian_defender = {'damage': 0, 'defense_up': 10, 'heal': 25}
            holy_nova = {'damage': 10, 'dmg_type': 'aoe', 'elemental_dmg': 10}
            sword = {'damage': 10, 'dmg_type': 'single_target'}
            class_skills = [holy_avenger, guardian_defender, holy_nova, sword]

            self.job_name = job_name
            self.hp_increase = 50
            self.str_increase = 2
            self.matk_increase = 1
            self.skills = class_skills

