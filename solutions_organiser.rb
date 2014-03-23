require 'fileutils'

class SolutionsOrganiser
  include FileUtils

  class FoldersOrganiser
    def initialize(solutions = Dir.glob("*.py"))
      @solutions = solutions
    end

    def organise_solutions
      @solutions.each do |solution|
        task_name = find_task_name(solution)
        create_and_change_dir(task_name)

        FileUtils.copy("../" + solution, 'solution.py')
        create_tests_structure(task_name)
        Dir.chdir('..')
      end
    end

    def create_folders_structure(solutions = true, tests = true)
      @solutions.each do |solution|
        create_and_change_dir(solution)

        create_solutions_structure(solution) if solutions
        create_tests_structure(solution)     if tests

        Dir.chdir('..')
      end
    end

    private

    def find_task_name(file_name)
      line = File.read(file_name).match(/print\(.*\(/)[0]
      line.match(/\(.*\(/)[0].delete('(')
    end

    def create_and_change_dir(name)
      Dir.mkdir(name)
      Dir.chdir(name)
    end

    def create_file_structure(file_name, template, dictionary = null)
      File.open(file_name, 'w') do |file|
        file.write(Templates.new.parse(template, dictionary))
      end
    end

    def create_solutions_structure(function_name)
      create_file_structure(
        'solution.py',
        Templates::FUNCTION_TEMPLATE,
        {function_name: function_name}
      )
    end

    def create_tests_structure(name)
      create_file_structure(
        'tests.py',
        Templates::TEST_TEMPLATE,
        {filename: name, filename_upper: Templates.new.to_camel_case(name)}
      )
    end

    class Templates
      MAIN_TEMPLATE = "
        |def main():
        |    pass
        |
        |if __name__ == '__main__':
        |    main()
      "

      FUNCTION_TEMPLATE = "
        |def %{function_name}():
        |    pass
        |
        |def main():
        |    print(%{function_name}())
        |
        |if __name__ == '__main__':
        |    main()
      "

      TEST_TEMPLATE = "
        |import unittest
        |from solution import %{filename}
        |
        |
        |class %{filename_upper}Test(unittest.TestCase):
        |    def setUp(self):
        |        pass
        |
        |    def test_%{filename}(self):
        |        self.assertEqual(, %{filename}())
        |
        |    def tearDown(self):
        |        pass
        |
        |if __name__ == '__main__':
        |    unittest.main()
      "

      def parse(template, dictionary = null)
        parsed = template.lines.map { |line| line.gsub(/.*\|/, '') }.join.strip
        dictionary ? parsed % dictionary : parsed
      end

      def to_camel_case(name)
        name.split('_').map{ |word| word.capitalize }.join
      end
    end
  end

  class GitOrganiser
    def initialize(solutions: nil)
      solutions = Dir.glob('*').select { |item| File.directory? item } if !solutions
      @solutions = solutions
    end

    def init
      system('git init')
    end

    def commit_solutions
      @solutions.each do |solution|
        system("git add #{solution}/")
        system("git commit -m 'Add solution and tests for #{solution}'")
      end
    end
  end

  class TestsRunner
    def initialize(solutions: nil)
      solutions = Dir.glob('*').select { |item| File.directory? item } if !solutions
      @solutions = solutions
    end

    def run_tests
      @solutions.each do |solution|
        puts "### Running tests for #{solution}"
        system("python #{solution}/tests.py")
        puts "\n\n"
      end
    end
  end
end

# SolutionsOrganiser::FoldersOrganiser.new.organise_solutions
solutions = [
  'simplify_fraction',
  'sort_fractions',
  'nth_fib_lists',
  'member_of_nth_fib_lists',
  'goldbach',
  'magic_square',
]
# SolutionsOrganiser::FoldersOrganiser.new(['sudoku_solved']).create_folders_structure
#
git_organiser = SolutionsOrganiser::GitOrganiser.new
git_organiser.init
git_organiser.commit_solutions
#
# SolutionsOrganiser::TestsRunner.new.run_tests
