from pathlib import Path


class ReportMerger:
    """
    Utility class to merge multiple ReportHtml results into a single
    report.
    """

    def __init__(self):
        self._report_paths = []

    def add_report(self, report_path):
        if isinstance(report_path, str):
            report_path = Path(report_path)
        self._report_paths.append(report_path)

    def generate_report(self, output_path):
        if isinstance(output_path, str):
            output_path = Path(output_path)

        self._extract_header_from_report(self._report_paths[0], output_path)

        for report_path in self._report_paths:
            self._extract_test_results_from_report(report_path, output_path)

        self._extract_footer_from_report(self._report_paths[0], output_path)

    def _extract_header_from_report(self, report_path, output_path):
        pass

    def _extract_test_results_from_report(self, report_path, output_path):
        pass

    def _extract_footer_from_report(self, report_path, output_path):
        pass
