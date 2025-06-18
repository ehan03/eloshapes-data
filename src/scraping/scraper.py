# standard library imports
import json
import os
from typing import Dict, List

# third party imports
import requests

# local imports
from ..config import API_KEY, DATA_DIR


class GamingMouseScraper:
    def __init__(self) -> None:
        self.url = "https://qyjffrmfirkwcwempawu.supabase.co/rest/v1/products_available_v2?select=general__id%2Cgeneral__handle%2Cgeneral__brand_handles%2Cgeneral__brand_names%2Cgeneral__brands_separator%2Cgeneral__model%2Cgeneral__variant%2Cgeneral__affiliate_links%2Cmouse__length%2Cmouse__width%2Cmouse__height%2Cmouse__shape%2Cmouse__hump_placement%2Cmouse__front_flare%2Cmouse__side_curvature%2Cmouse__hand_compatibility%2Cmouse__thumb_rest%2Cmouse__ring_finger_rest%2Cmouse__wireless%2Cmouse__weight%2Cmouse__dpi%2Cmouse__polling_rate%2Cmouse__side_buttons%2Cmouse__middle_buttons%2Cmouse__top_view%2Cmouse__side_view%2Cmouse__material_handle_general%2Cmouse__material_handle_specific%2Cmouse__material_name_general%2Cmouse__material_name_specific%2Cmouse__sensor_id%2Cmouse__sensor_parent_id%2Cmouse__sensor_handle%2Cmouse__sensor_brand_names%2Cmouse__sensor_brands_separator%2Cmouse__sensor_model%2Cmouse__sensor_variant%2Cmouse__sensor_rank%2Cmouse__sensor_type%2Cmouse__sensor_tracking_speed%2Cmouse__sensor_acceleration%2Cmouse__adjustable_sensor_position%2Cmouse__sensor_position_x%2Cmouse__sensor_position_x2%2Cmouse__sensor_position_y%2Cmouse__sensor_position_y2&general__category=eq.mouse&order=general__status_edited_date.desc"
        self.headers = {
            "Apikey": API_KEY,
        }
        self.file_path = os.path.join(DATA_DIR, "raw", "gaming_mice.json")

    def _fetch_data(self) -> List[Dict]:
        response = requests.get(self.url, headers=self.headers)

        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch data: {response.status_code} - {response.text}"
            )

        data = response.json()

        return data

    def _save_data(self, data: List[Dict]) -> None:
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def scrape(self) -> None:
        data = self._fetch_data()
        self._save_data(data)


if __name__ == "__main__":
    scraper = GamingMouseScraper()
    scraper.scrape()
