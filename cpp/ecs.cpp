struct Position
{
    float x;
    float y;
};
struct Velocity
{
    float x;
    float y;
};
struct Acceleration
{
    float x;
    float y;
};
class Entity
{
public:
    Position pos;
    Velocity vel;
    Acceleration accl;
};

#include <iostream>
#include <chrono>
#include <vector>

void update(std::vector<Entity> &ents)
{
    for (auto ent : ents)
    {
        ent.pos.x += ent.vel.x;
        ent.pos.y += ent.vel.y;

        ent.vel.x += ent.accl.x;
        ent.vel.y += ent.accl.y;
    }
}
void update_ecs(std::vector<Position> &poss, std::vector<Velocity> &vels, std::vector<Acceleration> &accls)
{
    for (size_t i = 0; i < poss.size(); i++)
    {
        poss[i].x += vels[i].x;
        poss[i].y += vels[i].y;
    }

    for (size_t i = 0; i < poss.size(); i++)
    {
        vels[i].x += accls[i].x;
        vels[i].y += accls[i].y;
    }
}

int main()
{
    const size_t N = 100000;

    std::vector<Entity> ents;

    for (size_t i = 0; i < N; i++)
    {
        ents.push_back(Entity());
    }

    std::vector<Position> ent_pos;
    std::vector<Velocity> ent_vel;
    std::vector<Acceleration> ent_accl;

    for (size_t i = 0; i < N; i++)
    {
        ent_pos.push_back(Position());
        ent_vel.push_back(Velocity());
        ent_accl.push_back(Acceleration());
    }

    std::cout << N << std::endl;

    auto prev1 = std::chrono::steady_clock::now();

    update(ents);

    auto now1 = std::chrono::steady_clock::now();

    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(now1 - prev1).count() << std::endl;

    auto prev2 = std::chrono::steady_clock::now();

    update_ecs(ent_pos, ent_vel, ent_accl);

    auto now2 = std::chrono::steady_clock::now();

    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(now2 - prev2).count() << std::endl;
}