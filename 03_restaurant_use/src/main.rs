use restaurant::front_of_house::hosting;
use restaurant::front_of_house::serving;
use restaurant::back_of_house;

fn main() {
    hosting::add_to_waitlist();
    hosting::seat_at_table();

    serving::take_order();
    serving::serve_order();
    serving::take_payment();

    back_of_house::take_care_trash();
}