# -*- coding:utf-8 -*-
"""
@Author  :   g1879
@Contact :   g1879@qq.com
"""
from os import popen
from pathlib import Path
from threading import Thread
from typing import Union, Tuple, List, Dict

from DownloadKit import DownloadKit
from requests import Session

from .chromium_base import ChromiumBase, ChromiumBaseSetter, ChromiumBaseWaiter, NetworkListener
from .chromium_driver import ChromiumDriver
from .chromium_tab import ChromiumTab
from .commons.web import DataPacket
from .configs.chromium_options import ChromiumOptions
from .configs.driver_options import DriverOptions
from .session_page import DownloadSetter


class ChromiumPage(ChromiumBase):

    def __init__(self,
                 addr_driver_opts: Union[str, int, ChromiumOptions, ChromiumDriver, DriverOptions] = None,
                 tab_id: str = None,
                 timeout: float = None):
        self._driver_options: [ChromiumDriver, DriverOptions] = ...
        self._process_id: str = ...
        self._window_setter: WindowSetter = ...
        self._main_tab: str = ...
        self._alert: Alert = ...
        self._download_path: str = ...
        self._download_set: ChromiumDownloadSetter = ...
        self._browser_driver: ChromiumDriver = ...
        self._rect: ChromiumTabRect = ...

    def _connect_browser(self,
                         addr_driver_opts: Union[str, ChromiumDriver, DriverOptions] = None,
                         tab_id: str = None) -> None: ...

    def _set_start_options(self, addr_driver_opts: Union[str, ChromiumDriver, DriverOptions], none) -> None: ...

    def _page_init(self) -> None: ...

    @property
    def browser_driver(self) -> ChromiumDriver: ...

    @property
    def tabs_count(self) -> int: ...

    @property
    def tabs(self) -> List[str]: ...

    @property
    def rect(self) -> ChromiumTabRect: ...

    @property
    def wait(self) -> ChromiumPageWaiter: ...

    @property
    def main_tab(self) -> str: ...

    @property
    def latest_tab(self) -> str: ...

    @property
    def process_id(self) -> Union[None, int]: ...

    @property
    def set(self) -> ChromiumPageSetter: ...

    @property
    def download_set(self) -> ChromiumDownloadSetter: ...

    @property
    def download(self) -> DownloadKit: ...

    @property
    def download_path(self) -> str: ...

    def get_tab(self, tab_id: str = None) -> ChromiumTab: ...

    def find_tabs(self, text: str = None, by_title: bool = True, by_url: bool = None,
                  special: bool = False) -> List[str]: ...

    def new_tab(self, url: str = None, switch_to: bool = True) -> str: ...

    def to_main_tab(self) -> None: ...

    def to_tab(self, tab_or_id: Union[str, ChromiumTab] = None, activate: bool = True) -> None: ...

    def _to_tab(self, tab_or_id: Union[str, ChromiumTab] = None, activate: bool = True,
                read_doc: bool = True) -> None: ...

    def close_tabs(self, tabs_or_ids: Union[
        str, ChromiumTab, List[Union[str, ChromiumTab]], Tuple[Union[str, ChromiumTab]]] = None,
                   others: bool = False) -> None: ...

    def close_other_tabs(self, tabs_or_ids: Union[
        str, ChromiumTab, List[Union[str, ChromiumTab]], Tuple[Union[str, ChromiumTab]]] = None) -> None: ...

    def handle_alert(self, accept: bool = True, send: str = None, timeout: float = None) -> Union[str, False]: ...

    def quit(self) -> None: ...

    def _on_alert_close(self, **kwargs): ...

    def _on_alert_open(self, **kwargs): ...


class ChromiumPageWaiter(ChromiumBaseWaiter):
    _driver: ChromiumPage = ...
    _listener: Union[NetworkListener, None] = ...

    def download_begin(self, timeout: float = None) -> bool: ...

    def new_tab(self, timeout: float = None) -> bool: ...

    def set_targets(self, targets: Union[str, list, tuple, set], is_regex: bool = False) -> None: ...

    def stop_listening(self) -> None: ...

    def data_packets(self, timeout: float = None,
                     any_one: bool = False) -> Union[DataPacket, Dict[str, List[DataPacket]], False]: ...


class ChromiumTabRect(object):
    def __init__(self, page: ChromiumPage):
        self._page: ChromiumPage = ...

    @property
    def window_state(self) -> str: ...

    @property
    def browser_location(self) -> Tuple[int, int]: ...

    @property
    def page_location(self) -> Tuple[int, int]: ...

    @property
    def viewport_location(self) -> Tuple[int, int]: ...

    @property
    def browser_size(self) -> Tuple[int, int]: ...

    @property
    def page_size(self) -> Tuple[int, int]: ...

    @property
    def viewport_size(self) -> Tuple[int, int]: ...

    @property
    def viewport_size_with_scrollbar(self) -> Tuple[int, int]: ...

    def _get_page_rect(self) -> dict: ...

    def _get_browser_rect(self) -> dict: ...


class ChromiumDownloadSetter(DownloadSetter):
    def __init__(self, page: ChromiumPage):
        self._page: ChromiumPage = ...
        self._behavior: str = ...
        self._download_th: Thread = ...
        self._session: Session = None
        self._waiting_download: bool = ...
        self._download_begin: bool = ...

    @property
    def session(self) -> Session: ...

    @property
    def _switched_DownloadKit(self) -> DownloadKit: ...

    def save_path(self, path: Union[str, Path]) -> None: ...

    def by_browser(self) -> None: ...

    def by_DownloadKit(self) -> None: ...

    def wait_download_begin(self, timeout: float = None) -> bool: ...

    def _cookies_to_session(self) -> None: ...

    def _download_by_DownloadKit(self, **kwargs) -> None: ...

    def _download_by_browser(self, **kwargs) -> None: ...

    def _wait_download_complete(self) -> None: ...


class Alert(object):

    def __init__(self):
        self.activated: bool = ...
        self.text: str = ...
        self.type: str = ...
        self.defaultPrompt: str = ...
        self.response_accept: str = ...
        self.response_text: str = ...


class WindowSetter(object):

    def __init__(self, page: ChromiumPage):
        self._page: ChromiumPage = ...
        self._window_id: str = ...

    def maximized(self) -> None: ...

    def minimized(self) -> None: ...

    def fullscreen(self) -> None: ...

    def normal(self) -> None: ...

    def size(self, width: int = None, height: int = None) -> None: ...

    def location(self, x: int = None, y: int = None) -> None: ...

    def hide(self) -> None: ...

    def show(self) -> None: ...

    def _get_info(self) -> dict: ...

    def _perform(self, bounds: dict) -> None: ...


def show_or_hide_browser(page: ChromiumPage, hide: bool = True) -> None: ...


def get_browser_progress_id(progress: Union[popen, None], address: str) -> Union[str, None]: ...


def get_chrome_hwnds_from_pid(pid: Union[str, int], title: str) -> list: ...


class ChromiumPageSetter(ChromiumBaseSetter):
    _page: ChromiumPage = ...

    def main_tab(self, tab_id: str = None) -> None: ...

    @property
    def window(self) -> WindowSetter: ...

    def tab_to_front(self, tab_or_id: Union[str, ChromiumTab] = None) -> None: ...
