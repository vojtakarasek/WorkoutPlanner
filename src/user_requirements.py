from body_part_enum import BodyPart
from level_enum import Level

class UserRequirements:
    def __init__(self, frame_instance):
        self.frame_instance = frame_instance
    
    def body_part_reqs(self) -> list[BodyPart]:
        body_parts = []
        selected_bp = self.frame_instance.combobox_variables_bp()
        for i in selected_bp:
            if len(i) == 0:
                pass
            else:
                body_parts.append(BodyPart(i))

        return body_parts

    def level_reqs(self):
        selected_lvl = self.frame_instance.combobox_variables_lvl()
        level = Level(selected_lvl)

        return level




