from starting_screen import Frame1
from body_part_enum import BodyPart


class UserRequirements:
    def requirements(self, frame1) -> list[BodyPart]:
        body_parts = []
        selected_bp = frame1.combobox_variables_bp()
        for i in selected_bp:
            if len(i) == 0:
                pass
            else:
                body_parts.append(BodyPart(i))

        return body_parts


frame1 = Frame1

