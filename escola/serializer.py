from rest_framework import serializers

from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    nivel = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'descricao', 'nivel']

    def get_nivel(self, obj):
        return obj.get_nivel_display()


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'curso', 'periodo']


class ListaMatriculaAlunosSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno_nome']
