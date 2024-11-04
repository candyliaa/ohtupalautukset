class Project:
    def __init__(
        self, name, description, license, authors, dependencies, dev_dependencies
    ):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, lis):
        return "\n- ".join(lis) if len(lis) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\nAuthors:\n- {self._stringify_list(self.authors)}"
            f"\nDependencies:\n- {self._stringify_list(self.dependencies)}"
            f"\nDevelopment Dependencies:\n- {self._stringify_list(self.dev_dependencies)}"
        )
