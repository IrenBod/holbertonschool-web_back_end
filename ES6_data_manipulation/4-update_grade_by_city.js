export default function updateStudentGradeByCity(list, city, newGrades) {
    if (!Array.isArray(list)) {
      return [];
    }
    return list
      .filter((student) => student.location === city)
      .map((student) => {
        const gradeObject = newGrades.find((grade) => grade.studentId === student.id);
        return {
          ...student,
          grade: gradeObject ? gradeObject.grade : 'N/A',
        };
      });
  }
