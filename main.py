from milky_way_main import *
import prob_calculator

def main():
    """Calculate detection probability & post galaxy display & statistics."""
    disc_radius_scaled, disc_vol_scaled = scale_galaxy()
    detection_prob = detect_prob(disc_vol_scaled)

    # build 4 main spiral arms & 4 trailing arms
    spirals(b=-0.3, r=disc_radius_scaled, rot_fac=2, fuz_fac=1.5, arm=0)
    spirals(b=-0.3, r=disc_radius_scaled, rot_fac=1.91, fuz_fac=1.5, arm=1)
    spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=2, fuz_fac=1.5, arm=0)
    spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=-2.09, fuz_fac=1.5, arm=1)
    spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=0.5, fuz_fac=1.5, arm=0)
    spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=0.4, fuz_fac=1.5, arm=1)
    spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=-0.5, fuz_fac=1.5, arm=0)
    spirals(b=-0.3, r=-disc_radius_scaled, rot_fac=-0.6, fuz_fac=1.5, arm=1)
    star_haze(disc_radius_scaled, density=8)

    # display legend
    c.create_text(-455, -360, fill='white', anchor='w',
                text='One Pixel = {} LY'.format(SCALE))
    c.create_text(-455, -330, fill='white', anchor='w',
                text='Radio Bubble Diameter = {} LY'.format(SCALE))
    c.create_text(-455, -300, fill='white', anchor='w',
                text='Probability of detection for {:,} civilizations = {}'.
                format(NUM_CIVS, detection_prob))

    # post Earth's 225 LY diameter bubble and annotate
    if SCALE == 225:
        c.create_rectangle(115, 75, 116, 76, fill='red', outline='')
        c.create_text(118, 72, fill='red', anchor='w',text="<---------- Earth's Radio Bubble")
    # run tkinter loop
    root.mainloop()

if __name__ == '__main__':
    main()
