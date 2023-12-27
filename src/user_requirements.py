from body_part_enum import BodyPart


class UserRequirements:
    def __init__(self, frame_instance):
        self.frame_instance = frame_instance
        self.body_parts = []
    
    def body_part_reqs(self) -> list[BodyPart]:
        self.body_parts = []
        selected_bp = self.frame_instance.combobox_variables_bp()
        for i in selected_bp:
            if len(i) == 0:
                pass
            else:
                self.body_parts.append(BodyPart(i))

        return self.body_parts




