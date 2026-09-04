import math

# formula 1 : Xbase = x*cos(theta) + z*sin(theta) + tx
# formula 2 : Ybase = y + ty
# formula 3 : Zbase = -x*sin(theta) + z*cos(theta) + tz


# input parameters
points = [[2.0, 0.0, -0.2], [3.5, 1.0, -0.3], [1.5, -0.8, -0.1]]
tx, ty, tz = 0.5, 0.0, 0.2
theta_deg = -15

def main(points , tx , ty , tz, theta_deg):

    theta = math.radians(theta_deg)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    for idx, point in enumerate(points, start=1):
        x, y, z = point

        # Formulas
        x_base = x * cos_t + z * sin_t + tx
        y_base = y + ty
        z_base = -x * sin_t + z * cos_t + tz

       

        print(f"Obstacle {idx}: {transformed_point}")

if __name__ == '__main__':
    main(points, tx, ty, tz , theta_deg)